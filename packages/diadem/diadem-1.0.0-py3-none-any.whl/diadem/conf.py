import os

from idem.conf import CLI_CONFIG
from idem.conf import CONFIG

WORD_LIST = "/usr/share/dict/words"

# Add subcommands to idem
SUBCOMMANDS = {
    "compile": {
        "help": "Parametrize and organize SLS files",
        "dyne": "idem",
    },
    "view": {
        "help": "Visualize relationships between resources",
        "dyne": "idem",
    },
}

# Patch idem's CLI config
for opt in (
    "tree",
    "sls",
    "params",
    "sls_sources",
    "param_sources",
    "render",
    "output",
):
    CLI_CONFIG[opt]["subcommands"] += ["compile", "view"]

CLI_CONFIG["arg_bind_strategy"] = {
    "subcommands": ["compile"],
    "loaded_mod_choices_ref": "idem.argbind_strategy",
}
CONFIG["arg_bind_strategy"] = {
    "help": "Strategy for replacing values with arg_bind statement",
    "default": "auto",
}

CLI_CONFIG["match_strategy"] = {
    "subcommands": ["compile"],
    "loaded_mod_choices_ref": "idem.match_strategy",
}

CONFIG["match_strategy"] = {
    "help": "Strategy for replacing shared resource attributes with params",
    "default": "clustering",
}

CLI_CONFIG["param_strategy"] = {
    "subcommands": ["compile"],
    "loaded_mod_choices_ref": "idem.param_strategy",
}

CONFIG["param_strategy"] = {
    "help": "Strategy for creating param keys",
    "default": "readable_hashing" if os.path.exists(WORD_LIST) else "hashing",
}

CLI_CONFIG["graph_layout"] = {
    "subcommands": ["view"],
    "choices": ["spring", "circular", "random", "shell", "kamada_kawai", "spectral"],
}

CONFIG["graph_layout"] = {
    "help": "Networkx graphing algorithm",
    "default": "spring",
}
CLI_CONFIG["show"] = {
    "subcommands": ["view"],
    "action": "store_true",
}

CONFIG["show"] = {
    "help": "Show the graph created by networkx",
    "default": False,
}

# Extend idem's namespace with the "diadem" directory
DYNE = {"idem": ["diadem"]}
