async def run(hub, graph_layout: str, show: bool, **kwargs) -> int:
    """
    Visualize relationships in SLS data using NetworkX and Matplotlib, focusing on resource_id relationships.
    Exclude orphan nodes from the graph and print them separately.
    """
    # Default to the yaml outputter
    output = hub.OPT.rend.output or "yaml"

    # Compile the data from idem
    data = await hub.idem.diadem.compile(**kwargs)

    G = hub.lib.nx.Graph()
    resource_ids = {}
    orphans = {}
    sharing_states = set()

    # First pass: Identify all resource_ids
    for state_id, state_data in data.items():
        for ref_func, attributes_list in state_data.items():
            for attributes in attributes_list:
                if "resource_id" in attributes:
                    resource_id = attributes["resource_id"]
                    if isinstance(resource_id, str):
                        ref = ref_func.rsplit(".", maxsplit=1)[0]
                        resource_ids[resource_id] = f"{ref}\n{state_id}"

    # Second pass: Find where these resource_ids are used in other resources
    for state_id, state_data in data.items():
        for ref_func, attributes_list in state_data.items():
            ref = ref_func.rsplit(".", maxsplit=1)[0]
            node_label = f"{ref}\n{state_id}"
            has_connections = False
            for attributes in attributes_list:
                for key, value in attributes.items():
                    if not isinstance(value, str):
                        continue
                    if value in resource_ids and key != "resource_id":
                        target_node = resource_ids[value]
                        new_state_id = target_node.split("\n")[1]
                        sharing_states.add(new_state_id)
                        if target_node != node_label:
                            G.add_edge(node_label, target_node)
                            has_connections = True
            if not has_connections:
                # Keep track of the orphan nodes
                orphans[state_id] = {f"{ref}.absent": attributes_list}

    # If a reosource id was part of another resource then it isn't an orphan
    for state_id in sharing_states:
        orphans.pop(state_id, None)

    # Print out the orphans
    out = hub.output[output].display(orphans)
    print(out)

    if show:
        if "plot" not in hub.idem:
            raise AttributeError(
                "Missing dependencies for 'idem view'.  Run 'pip install diadem[visualize].'"
            )
        # Draw the graph excluding orphans
        graph_function = getattr(hub.lib.nx, f"{graph_layout}_layout")
        pos = graph_function(G)
        hub.lib.nx.draw(G, pos, with_labels=True, font_weight="bold")
        edge_labels = hub.lib.nx.get_edge_attributes(G, "label")
        hub.lib.nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        hub.lib.matplot.pyplot.show()
    return 0
