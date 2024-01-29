def resolve(
    hub,
    clusters: list[dict[str, any]],
    cluster_map: dict[str, tuple[set[str], set[str]]],
) -> dict[int, str]:
    "Perform semantic analysis on the keys and values to create more contextually relevant and human-readable names."
    ref_map = {}

    for cluster_index, (_, refs) in cluster_map.items():
        ref = hub.idem.parametrize.most_common_path(refs)
        cluster = clusters[cluster_index]

        # Identify the most distinctive key in the cluster
        distinctive_key = max(cluster, key=lambda k: len(str(cluster[k])))
        distinctive_value = cluster[distinctive_key]

        # Convert complex types to a string representation
        if isinstance(distinctive_value, (list, dict)):
            distinctive_value_str = hub.lib.json.dumps(
                distinctive_value, sort_keys=True
            )
        else:
            distinctive_value_str = str(distinctive_value)

        # Create a readable name from the distinctive key-value pair
        semantic_name = f"{distinctive_key}.{distinctive_value_str}".replace(" ", "_")
        semantic_name = hub.lib.re.sub(r"[^a-zA-Z0-9_.]", "_", semantic_name)
        semantic_name = hub.lib.re.sub(r"_{2,}", "_", semantic_name).strip("_")

        # Form the ref_map key using the common ref path and semantic name
        ref_map_key = f"{ref}.{semantic_name}" if ref else semantic_name

        if ref_map_key in ref_map.values():
            ref_map_key = f"{ref_map_key}_{cluster_index}"

        ref_map[cluster_index] = ref_map_key

    return ref_map
