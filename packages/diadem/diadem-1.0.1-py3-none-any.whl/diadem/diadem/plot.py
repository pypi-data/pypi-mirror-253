def __virtual__(hub):
    """
    Add python imports to hub.lib that will be used by this module
    """
    hub.pop.sub.add(dyne_name="lib")
    hub.pop.sub.add(python_import="importlib", sub=hub.lib)
    try:
        hub.pop.sub.add(python_import="matplotlib", subname="matplot", sub=hub.lib)
        hub.lib.importlib.import_module("matplotlib.cm")
        hub.lib.importlib.import_module("matplotlib.colors")
        hub.lib.importlib.import_module("matplotlib.pyplot")
        return True
    except ImportError as e:
        return False, str(e)


def show(hub, G, graph_layout: str):
    graph_function = getattr(hub.lib.nx, f"{graph_layout}_layout")
    pos = graph_function(G)
    hub.lib.nx.draw(G, pos, with_labels=True, font_weight="bold")
    edge_labels = hub.lib.nx.get_edge_attributes(G, "label")
    hub.lib.nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    hub.lib.matplot.pyplot.show()
