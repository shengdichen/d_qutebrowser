class Alias:
    def __init__(self, config):
        self._config = config

    def apply(self) -> None:
        self._config.set(
            "aliases",
            {
                "q": "close",
                "qa": "quit",
                "w": "session-save",
                "wq": "quit --save",
                "wqa": "quit --save",
            },
        )
