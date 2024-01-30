def resolve(
    hub,
    clusters: list[dict[str, any]],
    cluster_map: dict[str, tuple[set[str], set[str]]],
) -> dict[int, str]:
    """
    Generate a hash from the cluster's content to ensure uniqueness, though this may sacrifice readability and meaning.
    """
    ref_map = {}

    for cluster_index, (_, refs) in cluster_map.items():
        ref = hub.idem.parametrize.most_common_path(refs)

        # Serialize the cluster and generate a hash
        serialized_cluster = hub.lib.json.dumps(clusters[cluster_index], sort_keys=True)
        cluster_hash = hub.lib.hash.sha256(serialized_cluster.encode()).hexdigest()[
            :8
        ]  # Shorten the hash for readability

        # Form the ref_map key using the common ref path and hash
        ref_map_key = f"{ref}.{cluster_hash}" if ref else cluster_hash

        ref_map[cluster_index] = ref_map_key

    return ref_map
