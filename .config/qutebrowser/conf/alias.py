class Alias:
    def __init__(self, config):
        self._config = config

        self._aliases = {}

    def apply(self) -> None:
        self._exit()
        self._tor_activate()
        self._tor_deactivate()

        self._config.set("aliases", self._aliases)

    def _exit(self) -> None:
        self._aliases |= {
            "w": "session-save",
            "wq": "quit --save",
            "q": "close",
            "q!": "quit",
        }

    def _tor_activate(self) -> None:
        cmd = " ".join(["set", "content.proxy", "socks://localhost:9050/"])
        self._aliases.update(tor_on=cmd)

    def _tor_deactivate(self) -> None:
        cmd = " ".join(["set", "content.proxy", "system"])
        self._aliases.update(tor_off=cmd)
