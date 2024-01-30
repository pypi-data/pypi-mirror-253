def resolve(hub, value, arg_bind: set[str]) -> str:
    """
    Try multiple strategies until one is a hit
    """
    for strategy in ("resource_id", "name", "ref_match"):
        ret = hub.idem.argbind_strategy[strategy].resolve(value, arg_bind)
        if ret:
            return ret
