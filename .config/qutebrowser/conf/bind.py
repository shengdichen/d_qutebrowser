class Bind:
    def __init__(self, config):
        self._config = config

    def apply(self):
        self._config.set(
            "bindings.key_mappings",
            {
                "<Ctrl+6>": "<Ctrl+^>",
                "<Ctrl+Enter>": "<Ctrl+Return>",
                "<Ctrl+i>": "<Tab>",
                "<Ctrl+j>": "<Return>",
                "<Ctrl+m>": "<Return>",
                "<Ctrl+[>": "<Escape>",
                "<Enter>": "<Return>",
                "<Shift+Enter>": "<Return>",
                "<Shift+Return>": "<Return>",
            },
        )

        # Bindings for normal mode
        self._config.bind("M", "hint links spawn mpv {hint-url}")

        self._config.bind("<Ctrl+h>", "tab-prev")
        self._config.bind("<Ctrl+l>", "tab-next")
        self._config.bind("K", self._concat(Bind._repeat("scroll up", 7)))
        self._config.bind("J", self._concat(Bind._repeat("scroll down", 7)))

    @staticmethod
    def _concat(commands: list[str]) -> str:
        return ";; ".join(commands)

    @staticmethod
    def _repeat(command: str, repeat_for: int) -> list[str]:
        return repeat_for * [command]
