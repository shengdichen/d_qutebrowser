from .util.cmd import Cmd


class ModeMulti:
    def __init__(self, config):
        self._config = config

        self._cmd_edit = "rl-"

        self._exit()
        self._navigate()
        self._edit()

    def _exit(self) -> None:
        cmd = "mode-leave"
        modes = ["command", "insert", "hint", "caret", "prompt", "register", "yesno"]

        for combi in ["<Ctrl+c>", "<Escape>"]:
            self._bind_modes(combi, cmd, modes)

    def _navigate(self) -> None:
        modes = ["command", "prompt"]

        self._bind_modes("<Ctrl+h>", f"{self._cmd_edit}backward-char", modes)
        self._bind_modes("<Ctrl+l>", f"{self._cmd_edit}forward-char", modes)
        self._bind_modes("<Ctrl+b>", f"{self._cmd_edit}backward-word", modes)
        self._bind_modes("<Ctrl+f>", f"{self._cmd_edit}forward-word", modes)
        self._bind_modes("<Ctrl+a>", f"{self._cmd_edit}beginning-of-line", modes)
        self._bind_modes("<Ctrl+e>", f"{self._cmd_edit}end-of-line", modes)

    def _edit(self) -> None:
        modes = ["command", "prompt"]

        self._bind_modes(
            "<Ctrl+j>", f"{self._cmd_edit}unix-line-discard", modes
        )  # delete  beg-o-l
        self._bind_modes(
            "<Ctrl+k>", f"{self._cmd_edit}kill-line", modes
        )  # delete until end-o-l
        self._bind_modes(
            "<Ctrl+w>", f'{self._cmd_edit}rubout " "', modes
        )  # delete until beg-o-w
        self._bind_modes(
            "<Ctrl+d>", f"{self._cmd_edit}kill-word", modes
        )  # delete until end-o-w

    def _bind_modes(self, combi: str, cmd: str, modes: list[str]) -> None:
        for mode in modes:
            self._config.bind(combi, cmd, mode=mode)


class _ModeSpecific:
    def __init__(self, mode: str, config):
        self._mode = mode
        self._config = config

    def _bind(self, combi: str, cmd: str = "") -> None:
        self._config.bind(combi, cmd, mode=self._mode)


class ModeCommand(_ModeSpecific):
    def __init__(self, config):
        super().__init__("command", config)

        self._basic()
        self._completion()

    def _basic(self) -> None:
        self._bind("<Return>", "command-accept")
        self._bind("<Ctrl+Return>", "command-accept --rapid")

    def _completion(self) -> None:
        cmd_completion = "completion-item-focus "
        self._bind("<Ctrl+p>", f"{cmd_completion} prev")
        self._bind("<Ctrl+n>", f"{cmd_completion} next")
        self._bind("<Shift+Tab>", f"{cmd_completion} prev-category")
        self._bind("<Tab>", f"{cmd_completion} next-category")

        self._bind("<Ctrl+k>", "command-history-prev")
        self._bind("<Ctrl+j>", "command-history-next")


class ModePrompt(_ModeSpecific):
    def __init__(self, config):
        super().__init__("prompt", config)

        self._basic()

    def _basic(self) -> None:
        self._bind("<Return>", "prompt-accept")

        self._bind("<Tab>", "prompt-item-focus next")
        self._bind("<Shift+Tab>", "prompt-item-focus prev")


class ModePassthrough(_ModeSpecific):
    def __init__(self, config):
        super().__init__("passthrough", config)

        self._exit()

    def _exit(self) -> None:
        self._bind("<Shift+Escape>", "mode-leave")


class Bind:
    def __init__(self, config):
        self._config = config
        self._remove_default()

    def _remove_default(self) -> None:
        self._config.set("bindings.default", {})

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

        self._navigation()
        self._command()
        self._open()
        self._gui()

        ModeMulti(self._config)
        self._mode_command()
        self._mode_prompt()
        ModePrompt(self._config)

    def _navigation(self) -> None:
        cmd_up, cmd_down = "scroll up", "scroll down"
        cmd_left, cmd_right = "scroll left", "scroll right"

        self._bind("k", cmd_up)
        self._bind("j", cmd_down)
        self._bind("h", cmd_left)
        self._bind("l", cmd_right)

        self._bind("K", self._concat(self._repeat(cmd_up, 7)))
        self._bind("J", self._concat(self._repeat(cmd_down, 7)))
        self._bind("H", self._concat(self._repeat(cmd_left, 4)))
        self._bind("L", self._concat(self._repeat(cmd_right, 4)))
        self._bind("<Ctrl+D>", "scroll-page 0 +0.5")
        self._bind("<Ctrl+U>", "scroll-page 0 -0.5")

        self._bind("gg", "scroll-to-perc 0")
        self._bind("G", "scroll-to-perc")

    def _command(self) -> None:
        self._bind(":", self._enter_as_prompt("", append_space=False))

    def _open(self) -> None:
        self._unbind(["o", "O"])
        self._bind("oo", self._enter_as_prompt(self._do_in_new_tab("")))
        self._bind("OO", self._enter_as_prompt("open --window"))

        self._bind("ob", self._enter_as_prompt("bookmark-load --tab"))
        self._bind("oB", self._enter_as_prompt("quickmark-load --tab"))

    @staticmethod
    def _do_in_new_tab(cmd: str) -> str:
        base = "open --tab"

        if not cmd:
            return base
        return Cmd.concat([base, cmd])

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

    def _mode_command(self) -> None:
        ModeCommand(self._config)

    def _mode_prompt(self) -> None:
        ModePrompt(self._config)
