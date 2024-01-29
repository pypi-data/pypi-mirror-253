def resolve(hub, flat: list[dict[str, any]]) -> list[dict[str, any]]:
    """
    Identify items that share the same key-value pairs and abstract them into a params statement
    """
