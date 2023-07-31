class Alias:
    def __init__(self, config):
        self._config = config

        self._aliases = {}
        self._exit()

    def _exit(self) -> None:
        self._aliases |= {
            "w": "session-save",
            "wq": "quit --save",
            "q": "close",
            "q!": "quit",
        }

    def apply(self) -> None:
        self._config.set("aliases", self._aliases)

    def add(self, name: str, cmd: str) -> None:
        self._aliases.update({name: cmd})
