def resolve(hub, flat: list[dict[str, any]]) -> list[dict[str, any]]:
    """
    Identify items that share the same key-value pairs and abstract them into a params statement
    """
    # Count the frequency of each key-value pair
    freq_counter = {}
    for item in flat:
        for key, value in item.items():
            freq_counter.setdefault((key, hub.lib.json.dumps(value)), 0)
            freq_counter[(key, hub.lib.json.dumps(value))] += 1

    # Group key-value pairs that appear frequently
    return [
        {k: hub.lib.json.loads(v)} for (k, v), freq in freq_counter.items() if freq > 1
    ]
