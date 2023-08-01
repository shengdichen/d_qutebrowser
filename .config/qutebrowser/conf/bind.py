from .util.cmd import Cmd


class _Util:
    @staticmethod
    def concat(commands: list[str]) -> str:
        return ";; ".join(commands)

    @staticmethod
    def repeat(command: str, repeat_for: int) -> list[str]:
        return repeat_for * [command]

    @staticmethod
    def enter_as_prompt(cmd: str, append_space: bool = True) -> str:
        base = "set-cmd-text "
        if append_space:
            return f"{base}--space :{cmd}"

        return f"{base}:{cmd}"

    @staticmethod
    def do_in_new_tab(cmd: str) -> str:
        base = "open --tab"

        if not cmd:
            return base
        return Cmd.concat([base, cmd])


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


class ModeNormal(_ModeSpecific):
    def __init__(self, config):
        super().__init__("normal", config)

        self._navigate()
        self._navigate_tab()
        self._command()
        self._open()
        self._hint()
        self._mark()
        self._gui()

    def _navigate(self) -> None:
        cmd_up, cmd_down = "scroll up", "scroll down"
        cmd_left, cmd_right = "scroll left", "scroll right"

        self._bind("k", cmd_up)
        self._bind("j", cmd_down)
        self._bind("h", cmd_left)
        self._bind("l", cmd_right)

        self._bind("K", _Util.concat(_Util.repeat(cmd_up, 7)))
        self._bind("J", _Util.concat(_Util.repeat(cmd_down, 7)))
        self._bind("H", _Util.concat(_Util.repeat(cmd_left, 4)))
        self._bind("L", _Util.concat(_Util.repeat(cmd_right, 4)))
        self._bind("u", "scroll-page 0 -0.5")
        self._bind("d", "scroll-page 0 +0.5")
        self._bind("b", "scroll-page 0 -1.0")
        self._bind("f", "scroll-page 0 +1.0")

        self._bind("gg", "scroll-to-perc 0")
        self._bind("G", "scroll-to-perc")

    def _navigate_tab(self) -> None:
        self._bind("<Ctrl+h>", "tab-prev")
        self._bind("<Ctrl+l>", "tab-next")

    def _command(self) -> None:
        self._bind(":", _Util.enter_as_prompt("", append_space=False))

    def _open(self) -> None:
        self._bind("o", _Util.enter_as_prompt(_Util.do_in_new_tab("")))
        self._bind("O", _Util.enter_as_prompt("open --window"))

    def _hint(self) -> None:
        self._bind("M", "hint links spawn mpv {hint-url}")

    def _mark(self) -> None:
        self._bind("ba", _Util.enter_as_prompt("bookmark-add"))
        self._bind("Ba", _Util.enter_as_prompt("quickmark-add"))

        self._bind("bo", _Util.enter_as_prompt("bookmark-load --tab"))
        self._bind("Bo", _Util.enter_as_prompt("quickmark-load --tab"))

    def _gui(self) -> None:
        self._bind("z", "gui_toggle")


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

        ModeMulti(self._config)
        ModeNormal(self._config)
        ModeCommand(self._config)
        ModePrompt(self._config)
        ModePrompt(self._config)

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
