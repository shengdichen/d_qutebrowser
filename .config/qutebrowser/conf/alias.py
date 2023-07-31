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
        cmd_show = Cmd.set_config_items(zip(items, ["always", "always"]))
        cmd_hide = Cmd.set_config_items(zip(items, ["never", "never"]))

        self._aliases |= {
            "gui_show": cmd_show,
            "gui_hide": cmd_hide,
        }

    def apply(self) -> None:
        self._config.set("aliases", self._aliases)

    def add(self, name: str, cmd: str) -> None:
        self._aliases.update({name: cmd})
