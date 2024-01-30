def resolve(
    hub,
    clusters: list[dict[str, any]],
    cluster_map: dict[str, tuple[set[str], set[str]]],
) -> dict[int, str]:
    """Analyze the frequency of keys and values across clusters to identify common patterns and use these to form the basis of the ref_map structure."""


def resolve(
    hub,
    clusters: list[dict[str, any]],
    cluster_map: dict[str, tuple[set[str], set[str]]],
) -> dict[int, str]:
    """
    Analyze the frequency of keys and values across clusters to identify common patterns and use these to form the basis of the ref_map structure.
    """
    ref_map = {}
    frequency_map = {}

    # Analyze frequency of keys and values in clusters
    for cluster in clusters:
        for key, value in cluster.items():
            # Convert lists and dicts to JSON strings for hashing
            if isinstance(value, (list, dict)):
                value = hub.lib.json.dumps(value, sort_keys=True)

            frequency_map.setdefault(key, {})
            frequency_map[key].setdefault(value, 0)
            frequency_map[key][value] += 1

    for cluster_index, (_, refs) in cluster_map.items():
        ref = hub.idem.parametrize.most_common_path(refs)

        # Find the most frequent key-value pair in the cluster
        cluster_keys = clusters[cluster_index].keys()
        most_common_pair = max(
            ((k, v) for k in cluster_keys for v, count in frequency_map[k].items()),
            key=lambda pair: frequency_map[pair[0]][pair[1]],
            default=None,
        )

        # Form the ref_map key using the common ref path and most common pair
        if most_common_pair:
            key, value = most_common_pair
            ref_map_key = f"{ref}.{key}.{value}" if ref else f"{key}.{value}"
        else:
            ref_map_key = f"{ref}._{cluster_index}" if ref else f"_{cluster_index}"

        if ref_map_key in ref_map.values():
            ref_map_key = f"{ref_map_key}_{cluster_index}"

        ref_map_key = ref_map_key.replace("-", "_")

        ref_map[cluster_index] = ref_map_key

    return ref_map
