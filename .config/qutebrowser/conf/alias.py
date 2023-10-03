from .util.cmd import Cmd


class Alias:
    def __init__(self, config):
        self._config = config

        self._aliases = {}
        self._exit()
        self._gui()
        self._hint()

    def _exit(self) -> None:
        cmd_history_clear = "history-clear --force"

        cmd_close_tab = "tab-close"
        self._aliases |= {
            "q": Cmd.concat([cmd_history_clear, cmd_close_tab]),
            "wq": Cmd.concat([cmd_history_clear, "bookmark-add", cmd_close_tab]),
        }

        session_name = "def"
        cmd_save = f"session-save {session_name}"
        self._aliases |= {
            "wa": Cmd.concat([cmd_history_clear, cmd_save]),
            "wqa": Cmd.concat([cmd_history_clear, f"quit --save {session_name}"]),
        }

        cmd_restart = "restart"
        self._aliases[cmd_restart] = Cmd.concat(
            [cmd_history_clear, cmd_save, cmd_restart]
        )

    def _gui(self) -> None:
        items = ["statusbar.show", "tabs.show"]
        states = ["always", "never"]

        self._aliases |= {
            "statusbar_toggle": Cmd.cycle_config_items(((items[0], states),)),
            "tabbar_toggle": Cmd.cycle_config_items(((items[1], states),)),
        }

    def _hint(self) -> None:
        base = "hint"
        name_to_op = {
            "jump": "normal",
            "tab": "tab-fg",
            "window": "window",
            "download": "download",
            "copy": "yank",
            "play": "spawn mpv {hint-url}",
            "hover": "hover",
        }

        commands = {}
        for name in name_to_op:
            commands[f"{base}_{name}"] = f"{base} all {name_to_op[name]}"
            commands[f"{base}_{name}_rapid"] = f"{base} all {name_to_op[name]} --rapid"

        self._aliases |= commands

    def apply(self) -> None:
        self._config.set("aliases", self._aliases)

    def add(self, name: str, cmd: str) -> None:
        self._aliases.update({name: cmd})
