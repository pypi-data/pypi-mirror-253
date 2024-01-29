def resolve(hub, value, arg_bind: set[str]) -> str:
    """
    If the last part of the ref in an arg_bind statement matches the data key, treat it as the source of truth.
    """
    for binding in arg_bind:
        ref, state_id, property_path = hub.lib.re.match(
            hub.idem.parametrize.ARG_BIND_MATCH, binding
        ).groups()
        resource_type = ref.split(".")[-1]
        if value and resource_type in str(value):
            return binding
