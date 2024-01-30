import os

WORD_LIST = "/usr/share/dict/words"


def __virtual__(hub):
    if os.path.exists(WORD_LIST):
        return True
    else:
        return False, "No unix word list found"


def resolve(
    hub,
    clusters: list[dict[str, any]],
    cluster_map: dict[str, tuple[set[str], set[str]]],
) -> dict[int, str]:
    """
    Create a unique and consistent set of words for each cluster based on a hash.
    """
    params = {}
    word_list = []

    # Load words from the Unix word list
    with open(WORD_LIST) as file:
        word_list = [word.strip() for word in file.readlines()]
    word_list_length = len(word_list)

    for cluster_index, (_, refs) in cluster_map.items():
        ref = hub.idem.parametrize.most_common_path(refs)

        # Generate a hash of the cluster data
        cluster_data = hub.lib.json.dumps(clusters[cluster_index], sort_keys=True)
        hash_value = int(hub.lib.hash.sha256(cluster_data.encode()).hexdigest(), 16)

        # Select words based on the hash
        first_word_index = hash_value % word_list_length
        second_word_index = -((hash_value // word_list_length) % word_list_length)

        first_word = word_list[first_word_index]
        second_word = word_list[second_word_index]

        # Form the params key using the common ref path and selected words
        params_key = (
            f"{ref}.{first_word}_{second_word}"
            if ref
            else f"{first_word}_{second_word}"
        )
        params_key = params_key.replace("'", "").lower()

        params[cluster_index] = params_key

    return params
