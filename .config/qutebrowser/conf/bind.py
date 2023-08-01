from .util.cmd import Cmd


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

        self._common()
        self._mode_command()

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

    def _common(self) -> None:
        for m in [
            "command",
            "insert",
            "hint",
            "caret",
            "prompt",
            "register",
            "yesno",
        ]:
            self._bind("<Escape>", "mode-leave", mode=m)

        self._bind("<Shift+Escape>", "mode-leave", mode="passthrough")

    def _mode_command(self) -> None:
        m = "command"

        self._bind("<Return>", "command-accept", mode=m)
        self._bind("<Ctrl+Return>", "command-accept --rapid", mode=m)

        cmd_completion = "completion-item-focus "
        self._bind("<Ctrl+p>", f"{cmd_completion} prev", mode=m)
        self._bind("<Ctrl+n>", f"{cmd_completion} next", mode=m)
        self._bind("<Shift+Tab>", f"{cmd_completion} prev-category", mode=m)
        self._bind("<Tab>", f"{cmd_completion} next-category", mode=m)

        self._bind("<Ctrl+k>", "command-history-prev", mode=m)
        self._bind("<Ctrl+j>", "command-history-next", mode=m)

        cmd_edit = "rl-"
        self._bind("<Ctrl+h>", f"{cmd_edit}backward-char", mode=m)
        self._bind("<Ctrl+l>", f"{cmd_edit}forward-char", mode=m)
        self._bind("<Ctrl+b>", f"{cmd_edit}backward-word", mode=m)
        self._bind("<Ctrl+f>", f"{cmd_edit}forward-word", mode=m)
        self._bind("<Ctrl+a>", f"{cmd_edit}beginning-of-line", mode=m)
        self._bind("<Ctrl+e>", f"{cmd_edit}end-of-line", mode=m)

        self._bind(
            "<Ctrl+j>", f"{cmd_edit}unix-line-discard", mode=m
        )  # delete  beg-o-l
        self._bind("<Ctrl+k>", f"{cmd_edit}kill-line", mode=m)  # delete until end-o-l
        self._bind("<Ctrl+w>", f'{cmd_edit}rubout " "', mode=m)  # delete until beg-o-w
        self._bind("<Ctrl+d>", f"{cmd_edit}kill-word", mode=m)  # delete until end-o-w
