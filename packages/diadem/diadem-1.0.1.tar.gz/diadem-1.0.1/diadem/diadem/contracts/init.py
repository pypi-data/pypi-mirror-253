def pre_cli_apply(hub, ctx):
    """
    If the subparser was defined by this project, then replace cli_apply with our patched version
    """
    if hub.SUBPARSER in ("view", "compile"):
        ctx.func = hub.idem.diadem.cli_apply.func


async def call_cli_apply(hub, ctx):
    """
    Pop calls Contracted.func, not ContractedContext.func, which is probably a bug.
    But until it's fixed we just need to make sure a call contract is available to run
    """
    return await ctx.func(*ctx.args, **ctx.kwargs)
