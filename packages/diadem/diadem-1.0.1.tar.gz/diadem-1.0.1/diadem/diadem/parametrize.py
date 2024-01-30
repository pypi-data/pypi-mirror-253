# Regular expression to extract state_ids, refs, and attributes from an arg_bind statement
ARG_BIND_MATCH = r"^\$\{([^:]+):([^:]+):(.+?)\}$"

# Regular expression to match the placeholder pattern with indentation capture
PLACEHOLDER_PATTERN = r"(\s+)-\s+__cluster_placeholder__:\s(\d+)"


async def run(
    hub,
    *,
    tree: str,
    arg_bind_strategy: str,
    match_strategy: str,
    param_strategy: str,
    **kwargs,
) -> int:
    """
    Executes the compilation and transformation of SLS data into a more manageable and parametrized format.

    This function performs several steps to optimize and restructure SLS data:
    1. Creates argbind relationships between resources.
    2. Flattens the data structure for pattern matching.
    3. Identifies common patterns and clusters them.
    4. Replaces original data with placeholders for matched clusters.
    5. Creates a unique key for each cluster and organizes them into a params structure.
    6. Replaces cluster placeholders with Jinja statements in the output.
    """
    # Default to the yaml outputter
    output = hub.OPT.rend.output or "yaml"

    data = await hub.idem.diadem.compile(**kwargs)
    hub.lib.copy.deepcopy(data)

    # Create argbind relationships between all the resources
    argbind = hub.idem.parametrize.arg_bind(data)

    # Iterate over the data and replace leaf nodes with arg_bind statements
    hub.idem.parametrize.replace_argbind(data, argbind, arg_bind_strategy)
    hub.idem.parametrize.drop_redundant_name(data)

    # Re-organize the data to be better suited for pattern matching
    flat = hub.idem.parametrize.flatten(data)

    # Identify common patterns between resources and cluster them into a list of param groups
    clusters = hub.idem.match_strategy[match_strategy].resolve(flat)

    # Replace the original data with placeholders for matched clusters
    cluster_map = hub.idem.parametrize.map_clusters(data, clusters)

    # Create a unique key for each cluster
    ref_map = hub.idem.param_strategy[param_strategy].resolve(clusters, cluster_map)

    # Organize the clusters that are used into an organized params structure
    params = hub.idem.parametrize.create_params(clusters, ref_map)

    # Only handle replacements for yaml data after it has been processed
    if not tree:

        # Output the argbind relationships to the cli in a single tree with the named outputter
        out = hub.output[output].display(data)
        # Replace all the cluster placeholders with proper jinja statements
        # This will only work properly for a yaml-like outputter
        out = hub.idem.parametrize.replace_jinja(out, clusters, params)

        print(out)
        print("-" * 80)
        out = hub.output[output].display(params)
        print(out)

    # If a tree root was given, then organize the new sls and params into trees and write both to files with the given outputter
    elif tree:
        t = hub.lib.pathlib.Path(tree)
        hub.idem.parametrize.write_sls_to_tree(t / "state", data, clusters, params)
        # write params to a tree
        hub.idem.parametrize.write_param_to_tree(t / "param", params)

    return 0


def arg_bind(hub, data: dict[str : dict[list[dict[str, any]]]]) -> dict[any, set[str]]:
    """
    Parse all the SLS data and express every value as an arg_bind statement
    """
    # Map raw values to an argbind statement that can retrieve that value from another state
    argbind: dict[any, set[str]] = {}

    for state_id, state in data.items():
        for state_ref, parameters in state.items():
            for parameter in parameters:
                for name, value in parameter.items():
                    # handle nested property paths
                    prop_paths = hub.idem.parametrize.prop(name, value)
                    for prop_path, property_value in prop_paths.items():
                        ref = state_ref.rsplit(".", maxsplit=1)[0]
                        argbind.setdefault(property_value, set()).add(
                            # Create an argbind reference in the format ${<ref>:<state_id>:<property_path>}
                            f"${{{ref}:{state_id}:{prop_path}}}"
                        )

    return argbind


def prop(hub, name: str, value: any) -> dict[str, any]:
    """
    Recursively construct property references for arg_binding
    """
    builder = {}

    if isinstance(value, dict):
        for path_addendum, property_value in value.items():
            builder.update(
                hub.idem.parametrize.prop(f"{name}:{path_addendum}", property_value)
            )
    elif isinstance(value, hub.lib.collections.abc.Iterable) and not isinstance(
        value, (str, bytes)
    ):
        for path_addendum, property_value in enumerate(value):
            builder.update(
                hub.idem.parametrize.prop(f"{name}:{path_addendum}", property_value)
            )
    else:
        # Base case for escaping recursion
        builder[name] = value

    return builder


def replace_argbind(
    hub,
    data: dict[str : dict[list[dict[str, any]]]],
    argbind: dict[any, set[str]],
    arg_bind_strategy: str,
):
    """
    "data" represents parsed, compiled, and combined SLS data.
    For each leaf node in the data, find out which arg bind statement for that value is a source of truth
    then perform the replacement
    """
    for value, arg_binds in argbind.items():
        # If there is only one instance of a value, it does not need arg_bind statements
        if not len(arg_binds) > 1:
            continue

        # Try to find a source of truth, a single arg_bind statement for the given value
        source_of_truth = hub.idem.argbind_strategy[arg_bind_strategy].resolve(
            value, arg_binds
        )
        # If we could not find out which arg_bind statement is a source of truth then move on
        if not source_of_truth:
            continue

        sot_ref, sot_state_id, sot_property_path = hub.lib.re.match(
            ARG_BIND_MATCH, source_of_truth
        ).groups()

        # Replace the value in data based on the arg_bind property
        for binding in arg_binds:
            # Skip the source of truth for arg bind -- somewhere has to contain the actual value
            if binding == source_of_truth:
                continue

            # Get the state_id and property_path from the arg_bind statement
            ref, state_id, property_path = hub.lib.re.match(
                ARG_BIND_MATCH, binding
            ).groups()

            # Don't bind a resource to itself if it has two keys with the same value
            if sot_state_id == state_id:
                continue

            properties = property_path.split(":")

            # Make sure the function name is preserved
            for full_ref in data[state_id]:
                if full_ref.startswith(f"r{ref}."):
                    break

            # Unravel the property path and use it to navigate to the right place in the data to drop in the source-of-truth arg_bind statement
            root = data[state_id][full_ref]

            for parameter in root:
                if properties[0] in parameter:
                    root = parameter
                    break
            else:
                continue

            for property in properties[:-1]:
                if property.isdigit():
                    property = int(property)
                root = root[property]

            # Process the last property separately so we can update the reference to the property within data
            property = properties[-1]
            if property.isdigit():
                property = int(property)

            # Perform the replacement
            root[property] = source_of_truth


def drop_redundant_name(
    hub,
    data: dict[str : dict[list[dict[str, any]]]],
):
    """
    When the "name" parameter is the same as the state_id, drop it
    """
    for state_id, state in data.items():
        for state_ref, parameters in state.items():
            # Initialize a new list to store parameters that don't have redundant names
            new_parameters = []
            for parameter in parameters:
                # Check if the parameter has a 'name' key and if it's equal to the state_id
                if parameter.get("name") != state_id:
                    # If the 'name' is not redundant, add the parameter to the new list
                    new_parameters.append(parameter)

            # Replace the old parameters list with the new list without redundant names after we are done iterating over parameters
            data[state_id][state_ref] = new_parameters


def flatten(hub, data: dict[str : dict[list[dict[str, any]]]]) -> list[dict[str, any]]:
    """
    Take the raw SLS data and flatten it into a structure that can be used for easy pattern matching to create params.

    - Remove the state ids, they are always unique.
    - Take the list of key/value pair dictionaries for the resource parameters and turn it into a plain dictionary.
    """
    result = []
    for resource_data in data.values():
        for attributes in resource_data.values():
            flattened_dict = {k: v for attr in attributes for k, v in attr.items()}
            result.append(flattened_dict)
    return result


def map_clusters(
    hub, data: dict[str : dict[list[dict[str, any]]]], clusters: list[dict[str, any]]
) -> dict[str, tuple[set[str], set[str]]]:
    """
    Maps each cluster to the state IDs and refs in the original data that contain the attributes of the cluster.

    Args:
        data: The original data structured as a dictionary.
        clusters: A list of dictionaries, each representing a cluster of shared attributes.

    Returns:
        A dictionary where each key is a cluster index, and the value is a tuple containing sets of state IDs and refs that use this cluster.
    """
    cluster_map = {}

    for cluster_index, cluster in enumerate(clusters):
        for state_id, state in data.items():
            for ref, attributes in state.items():
                # Flatten the attributes for comparison
                flattened_attributes = {
                    k: v for attr in attributes for k, v in attr.items()
                }

                # Check if the resource data contains all items in the cluster
                if all(
                    item in flattened_attributes.items() for item in cluster.items()
                ):
                    # Create a list of keys to be removed to avoid modifying the dict while iterating
                    keys_to_remove = [
                        key for key in cluster.keys() if key in flattened_attributes
                    ]

                    # Remove shared attributes and track if any attribute was removed
                    attribute_removed = False
                    for key in keys_to_remove:
                        for attr in attributes:
                            if key in attr:
                                attr.pop(key)
                                attribute_removed = True

                    # Replace with cluster placeholder and index if any attribute was removed
                    if attribute_removed:
                        attributes.append({"__cluster_placeholder__": cluster_index})

                        # Update mapping
                        if cluster_index not in cluster_map:
                            cluster_map[cluster_index] = (set(), set())
                        cluster_map[cluster_index][0].add(state_id)
                        cluster_map[cluster_index][1].add(ref)

            # Cleanup: Remove empty dictionaries from attributes
            for ref, attrs in state.items():
                state[ref] = [attr for attr in attrs if attr]

    return cluster_map


def most_common_path(hub, refs: set[str]) -> str:
    """
    Determines a common path based on the shared parts of resource references.
    """
    if not refs:
        return ""

    # Split the first reference to get the parts
    first_ref_parts = next(iter(refs)).split(".")

    # Iterate over parts and check if they are common in all refs
    common_parts = []
    for part in first_ref_parts:
        if all(part in ref.split(".") for ref in refs):
            common_parts.append(part)
        else:
            break

    return ".".join(common_parts)


def create_params(
    hub, clusters: list[dict[str, any]], ref_map: dict[int, str]
) -> dict[str, ...]:
    params = {}

    for cluster_index, param_ref in ref_map.items():
        keys = param_ref.split(".")

        # Construct the shared data structure for params
        root = params
        for key in keys[:-1]:
            if key not in root:
                root[key] = {}
            root = root[key]

        # The last key in the ref is where we want to put the param values
        root[keys[-1]] = clusters[cluster_index]

    return params


def replace_jinja(
    hub, yaml_output: str, clusters: list[dict[str, any]], params: dict[str, ...]
):
    """
    Replace cluster placeholders in the YAML string with Jinja statements.
    """

    def _replace_match(match: hub.lib.re.Match):
        # Function to replace each match
        cluster_index = int(match.group(2))
        attr_values = clusters[cluster_index]

        # Find the path to attr_values in params
        param_path_to_attr_values = hub.idem.parametrize.search_params(
            attr_values, params
        )
        if not param_path_to_attr_values:
            # Return original string if path not found
            return match.group(0)

        # Construct the Jinja statement with correct indentation
        indent = match.group(1)
        jinja_statement = f"{indent}{{% for key, value in params.{param_path_to_attr_values}.items() %}}{indent}- {{{{ key }}}}: {{{{ value }}}}{indent}{{% endfor %}}"
        return jinja_statement

    # Replace all matches in the YAML string
    return hub.lib.re.sub(PLACEHOLDER_PATTERN, _replace_match, yaml_output)


def search_params(
    hub, target: dict[str, ...], current_params: dict[str, ...], current_path: str = ""
) -> str:
    """
    Recursively search for the target in the params and return the path.
    """
    if target == current_params:
        return current_path

    if isinstance(current_params, dict):
        for key, value in current_params.items():
            path = hub.idem.parametrize.search_params(
                target, value, current_path + (f".{key}" if current_path else key)
            )
            if path:
                return path


def write_sls_to_tree(
    hub,
    tree: "pathlib.Path",
    data: dict[str : dict[list[dict[str, any]]]],
    clusters: list[dict[str, any]],
    params: dict[str, ...],
):
    """
    Write SLS data to a tree structure on the filesystem using pathlib.

    Args:
        tree: The root directory where the tree structure will be created.
        data: The SLS data to be written, organized in a nested dictionary format.
    """

    for state_id, state in data.items():
        for ref in state:
            parts = ref.split(".")

            # The last item in the ref is the function name.
            # The second to last is the leaf node
            dirs = parts[:-2]
            sls_file = f"{parts[-2]}.sls"

            node_path = tree
            for d in dirs:
                next_node_path = node_path / d
                if not next_node_path.exists():
                    next_node_path.mkdir(exist_ok=True, parents=True)
                    _update_init_file(node_path, d)

                node_path = next_node_path

            sls = node_path / sls_file
            if not sls.exists():
                sls.touch()
                _update_init_file(node_path, sls.stem)

            out = hub.output.yaml.display({state_id: {ref: state[ref]}})
            out = hub.idem.parametrize.replace_jinja(out, clusters, params)

            with sls.open("a") as fh:
                fh.write(out)


def _update_init_file(parent_path: "pathlib.Path", child_name: str):
    """
    Update the init.sls file in the parent directory to include the child directory or file.
    """
    init_file = parent_path / "init.sls"
    include_line = f"  - .{child_name}\n"

    if not init_file.exists():
        with init_file.open("w") as fh:
            fh.write("include:\n")
            fh.write(include_line)
    else:
        with init_file.open("r+") as fh:
            content = fh.read()
            if include_line not in content:
                fh.seek(0, 2)  # Move to the end of the file
                fh.write(include_line)


def write_param_to_tree(
    hub,
    tree: "pathlib.Path",
    params: dict[str, ...],
):
    """
    Write params data to a tree structure on the filesystem using pathlib.

    Args:
        tree: The root directory where the tree structure will be created.
        params: The params data to be written, organized in a nested dictionary format.
    """

    for top_level_key, param_data in params.items():
        param_file = f"{top_level_key}.sls"
        file_path = tree / param_file
        file_path.parent.mkdir(exist_ok=True, parents=True)

        if not file_path.exists():
            file_path.touch()
            _update_init_file(tree, top_level_key)

        out = hub.output.yaml.display({top_level_key: param_data})

        with file_path.open("a") as fh:
            fh.write(out)
