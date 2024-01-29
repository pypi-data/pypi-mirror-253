def resolve(hub, value, arg_bind: set[str]) -> str:
    """
    If there is an arg_bind statement with a "name", treat it as the source of truth
    """
    for binding in arg_bind:
        ref, state_id, property_path = hub.lib.re.match(
            hub.idem.parametrize.ARG_BIND_MATCH, binding
        ).groups()
        if property_path == "name":
            return binding
