from .util.cmd import Cmd


class Alias:
    def __init__(self, config):
        self._config = config

        self._aliases = {}
        self._exit()
        self._gui()
        self._hint()

    def _exit(self) -> None:
        session_name = "def"
        cmd_history_clear = "history-clear --force"

        self._aliases |= {
            "w": Cmd.concat([cmd_history_clear, f"session-save {session_name}"]),
            "wq": Cmd.concat([cmd_history_clear, f"quit --save {session_name}"]),
            "q": "tab-close",
        }

    def _gui(self) -> None:
        items = ["statusbar.show", "tabs.show"]
        states = ["always", "never"]
        cmd_toggle = Cmd.cycle_config_items(zip(items, 2 * [states]))
        cmd_show = Cmd.set_config_items(zip(items, 2 * [states[0]]))
        cmd_hide = Cmd.set_config_items(zip(items, 2 * [states[1]]))

        self._aliases |= {
            "gui_show": cmd_show,
            "gui_hide": cmd_hide,
            "gui_toggle": cmd_toggle,
        }

    def _hint(self) -> None:
        base = "hint"
        hint_links, hint_inputs, hint_all = "links", "inputs", "all"

        self._aliases |= {
            f"{base}_{hint_type}_rapid": f"{base} {hint_type} tab-bg --rapid"
            for hint_type in [hint_links, hint_all]
        }

        self._aliases |= {f"{base}_mpv": f"{base} {hint_links} spawn mpv {{hint-url}}"}

    def apply(self) -> None:
        self._config.set("aliases", self._aliases)

    def add(self, name: str, cmd: str) -> None:
        self._aliases.update({name: cmd})
