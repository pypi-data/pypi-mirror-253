def resolve(
    hub,
    clusters: list[dict[str, any]],
    cluster_map: dict[str, tuple[set[str], set[str]]],
) -> dict[int, str]:
    """
    Use a concatenation of attribute keys to form unique identifiers, especially useful when clusters have similar values but different sets of keys.
    """
    ref_map = {}

    for cluster_index, (_, refs) in cluster_map.items():
        ref = hub.idem.parametrize.most_common_path(refs)

        # Concatenate attribute keys from the cluster
        keys = sorted(clusters[cluster_index].keys())
        keys_concat = "_".join(keys)

        # Form the ref_map key using the common ref path and concatenated keys
        ref_map_key = f"{ref}.{keys_concat}" if ref else keys_concat

        if ref_map_key in ref_map.values():
            ref_map_key = f"{ref_map_key}_{cluster_index}"

        ref_map[cluster_index] = ref_map_key

    return ref_map
