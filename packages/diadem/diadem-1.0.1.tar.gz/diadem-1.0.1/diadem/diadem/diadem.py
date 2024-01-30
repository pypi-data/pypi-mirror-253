def __init__(hub):
    """
    Initialize imports and structures that will be used by the whole project
    """
    # Create a sub for python imports
    hub.pop.sub.add(dyne_name="lib")
    hub.pop.sub.add(python_import="importlib", sub=hub.lib)
    hub.pop.sub.add(python_import="collections", sub=hub.lib)
    hub.lib.importlib.import_module("collections.abc")
    hub.pop.sub.add(python_import="copy", sub=hub.lib)
    hub.pop.sub.add(python_import="hashlib", subname="hash", sub=hub.lib)
    hub.pop.sub.add(python_import="itertools", sub=hub.lib)
    hub.pop.sub.add(python_import="json", sub=hub.lib)
    hub.pop.sub.add(python_import="networkx", subname="nx", sub=hub.lib)
    hub.pop.sub.add(python_import="pathlib", sub=hub.lib)
    hub.pop.sub.add(python_import="pprint", sub=hub.lib)
    hub.pop.sub.add(python_import="random", sub=hub.lib)
    hub.pop.sub.add(python_import="re", sub=hub.lib)


async def cli_apply(hub) -> int:
    """
    A patch for idem's cli_apply function that runs when diadem's subcommands are specified
    """
    if hub.SUBPARSER == "compile":
        return await hub.idem.parametrize.run(**hub.OPT.idem)
    if hub.SUBPARSER == "view":
        return await hub.idem.visualize.run(**hub.OPT.idem)


async def compile(
    hub,
    *,
    run_name: str,
    render: str,
    sls_sources: list[str],
    param_sources: list[str],
    sls: list[str],
    params: list[str] = None,
    **kwargs,
) -> int:
    """
    From the SLS sources and param sources, create a new high data tree with idem.
    """
    if params is None:
        params = []

    # Combine sls and param sources into single trees
    src = hub.idem.sls_source.init.get_refs(sources=sls_sources, refs=sls)
    param = hub.idem.sls_source.param.get_refs(sources=param_sources, refs=params)

    await hub.idem.state.create(
        run_name,
        src["sls_sources"],
        render=render,
        runtime=None,
        subs=["states"],
        cache_dir=None,
        test=None,
        acct_file=None,
        acct_key=None,
        acct_profile=None,
        acct_blob=None,
        managed_state=None,
        param_sources=param["param_sources"],
    )

    if params:
        await hub.idem.sls_source.param.gather(run_name, *params)

    # Get the sls file, render it, compile high data to "new" low data tree
    await hub.idem.sls_source.init.gather(run_name, *sls)

    if hub.idem.RUNS[run_name]["errors"]:
        errors = "\n- ".join(hub.idem.RUNS[run_name]["errors"])
        raise RuntimeError(f"Encountered errors when compiling SLS data: {errors}")

    # Pass the states through idem's native compile process.
    # This will not take into account reconciliation (since the states are not being run) or delayed rendering
    await hub.idem.state.compile(run_name)
    low = hub.idem.RUNS[run_name]["low"]
    seq = hub.idem.req.seq.init.run(None, low, hub.idem.RUNS[run_name]["running"], {})

    # Re-organize the sequenced low-data to just what we need to parametrize and organize it
    result = {}
    for compiled_state in seq.values():
        chunk = compiled_state["chunk"]

        result[chunk["__id__"]] = {
            f'{chunk["state"]}.{chunk["fun"]}': [
                {k: v}
                for k, v in chunk.items()
                if k not in ("__id__", "__sls__", "fun", "order", "state")
            ]
        }

    return result
