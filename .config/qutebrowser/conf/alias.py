from .util.cmd import Cmd


class Alias:
    def __init__(self, config):
        self._config = config

        self._aliases = {}
        self._exit()
        self._gui()

    def _exit(self) -> None:
        self._aliases |= {
            "w": "session-save def",
            "wq": "quit --save def",
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

    def apply(self) -> None:
        self._config.set("aliases", self._aliases)

    def add(self, name: str, cmd: str) -> None:
        self._aliases.update({name: cmd})
