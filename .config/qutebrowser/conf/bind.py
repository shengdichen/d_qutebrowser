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

        self._unbind("d")

        self._open()
        self._gui()

    def _open(self) -> None:
        self._unbind(["o", "O"])
        self._bind("o", self._enter_as_prompt("open --tab"))

    def _gui(self) -> None:
        self._bind("z", "gui_toggle")

    @staticmethod
    def _concat(commands: list[str]) -> str:
        return ";; ".join(commands)

    @staticmethod
    def _repeat(command: str, repeat_for: int) -> list[str]:
        return repeat_for * [command]

    def _bind(self, combi: str, cmd: str = "", mode: str = "normal") -> None:
        if not cmd:
            self._unbind(combi, mode)
        else:
            self._config.bind(combi, cmd, mode)

    def _unbind(self, combis: list[str] | str, mode: str = "normal") -> None:
        if isinstance(combis, str):
            combis = [combis]

        for combi in combis:
            self._config.bind(combi, "nop", mode)

    @staticmethod
    def _enter_as_prompt(cmd: str, append_space: bool = True) -> str:
        base = "set-cmd-text "
        if append_space:
            return f"{base}--space :{cmd}"

        return f"{base}:{cmd}"
