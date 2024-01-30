def resolve(
    hub,
    clusters: list[dict[str, any]],
    cluster_map: dict[str, tuple[set[str], set[str]]],
) -> dict[int, str]:
    "Use simple numerical indexing"
    ref_map = {}

    for cluster_index, (_, refs) in cluster_map.items():
        ref = hub.idem.parametrize.most_common_path(refs)

        # Use simple numerical indexing for the final part of the path
        ref_map_key = f"{ref}._{cluster_index}"
        ref_map[cluster_index] = ref_map_key

    return ref_map
