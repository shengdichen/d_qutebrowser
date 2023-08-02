from .util.cmd import Cmd


class _Util:
    _key_translation: dict = {
        "esc": "Escape",
        "enter": "Return",
        "tab": "Tab",
        "space": "Space",
    }

    _decorator_translation: dict = {"c": "Ctrl", "s": "Shift", "a": "Alt"}

    def __init__(self, config):
        self._config = config

    @staticmethod
    def make_combi(key_base: str, decorators: str = None) -> str:
        if decorators is None:
            if key_base in _Util._key_translation:
                return f"<{_Util._key_translation[key_base]}>"
            return key_base

        decorators_translated = "+".join(
            (_Util._decorator_translation.get(decorator) for decorator in decorators)
        )
        key_translated = _Util._key_translation.get(key_base, key_base)
        return f"<{decorators_translated}+{key_translated}>"

    def bind(self, combis: list[str] | str, cmd: str, mode: str) -> None:
        if isinstance(combis, str):
            combis = [combis]

        if not cmd:
            self.unbind(combis, mode)
        else:
            for combi in combis:
                self._config.bind(combi, cmd, mode)

    def unbind(self, combis: list[str] | str, mode: str) -> None:
        if isinstance(combis, str):
            combis = [combis]

        for combi in combis:
            self._config.bind(combi, "nop", mode)


class ModeMulti:
    def __init__(self, config):
        self._config = config

        self._cmd_edit = "rl-"

        self._exit()
        self._navigate()
        self._edit()

    def _exit(self) -> None:
        cmd = "mode-leave"
        modes = ["command", "hint", "caret", "prompt", "register", "yesno"]

        for combi in [_Util.make_combi("c", decorators="c"), _Util.make_combi("esc")]:
            self._bind_modes(combi, cmd, modes)

    def _navigate(self) -> None:
        modes = ["command", "prompt"]

        self._bind_modes(
            _Util.make_combi("h", decorators="c"),
            f"{self._cmd_edit}backward-char",
            modes,
        )
        self._bind_modes(
            _Util.make_combi("l", decorators="c"),
            f"{self._cmd_edit}forward-char",
            modes,
        )
        self._bind_modes(
            _Util.make_combi("b", decorators="c"),
            f"{self._cmd_edit}backward-word",
            modes,
        )
        self._bind_modes(
            _Util.make_combi("f", decorators="c"),
            f"{self._cmd_edit}forward-word",
            modes,
        )
        self._bind_modes(
            _Util.make_combi("a", decorators="c"),
            f"{self._cmd_edit}beginning-of-line",
            modes,
        )
        self._bind_modes(
            _Util.make_combi("e", decorators="c"), f"{self._cmd_edit}end-of-line", modes
        )

    def _edit(self) -> None:
        modes = ["command", "prompt"]

        self._bind_modes(
            _Util.make_combi("j", decorators="c"),
            f"{self._cmd_edit}unix-line-discard",
            modes,
        )  # delete  beg-o-l
        self._bind_modes(
            _Util.make_combi("k", decorators="c"), f"{self._cmd_edit}kill-line", modes
        )  # delete until end-o-l
        self._bind_modes(
            _Util.make_combi("w", decorators="c"), f'{self._cmd_edit}rubout " "', modes
        )  # delete until beg-o-w
        self._bind_modes(
            _Util.make_combi("d", decorators="c"), f"{self._cmd_edit}kill-word", modes
        )  # delete until end-o-w

    def _bind_modes(self, combis: list[str] | str, cmd: str, modes: list[str]) -> None:
        for mode in modes:
            _Util(self._config).bind(combis, cmd, mode=mode)


class _ModeSpecific:
    def __init__(self, mode: str, config):
        self._mode = mode
        self._config = config

    def _bind(self, combis: list[str] | str, cmd: str = "") -> None:
        _Util(self._config).bind(combis, cmd, mode=self._mode)


class ModeNormal(_ModeSpecific):
    def __init__(self, config):
        super().__init__("normal", config)

        self._navigate()
        self._search()
        self._hint()
        self._macro()
        self._navigate_tab()
        self._to_other_modes()
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

        self._bind("K", Cmd.concat(Cmd.repeat(cmd_up, 7)))
        self._bind("J", Cmd.concat(Cmd.repeat(cmd_down, 7)))
        self._bind("H", Cmd.concat(Cmd.repeat(cmd_left, 4)))
        self._bind("L", Cmd.concat(Cmd.repeat(cmd_right, 4)))

        cmd_scroll = "scroll-page "
        self._bind("u", f"{cmd_scroll}0 -0.37")
        self._bind("d", f"{cmd_scroll}0 +0.37")
        self._bind("b", f"{cmd_scroll}0 -1.0")
        self._bind("f", f"{cmd_scroll}0 +1.0")

        cmd_scroll_perc = "scroll-to-perc "
        self._bind("gg", f"{cmd_scroll_perc} 0")
        self._bind("G", f"{cmd_scroll_perc} 100")

    def _search(self) -> None:
        self._bind("/", "set-cmd-text /")
        self._bind("?", "set-cmd-text ?")

        self._bind("n", "search-next")
        self._bind("N", "search-prev")

        cmd_follow = "selection-follow"
        self._bind(_Util.make_combi("enter"), "selection-follow")
        self._bind(_Util.make_combi("enter", decorators="c"), f"{cmd_follow} --tab")

    def _hint(self) -> None:
        base = "hint "

        self._bind("ti", f"{base}inputs")

        hint_links, hint_all = "links", "all"
        self._bind("tt", f"{base}{hint_links}")
        self._bind("ta", f"{base}{hint_all}")

        in_tab = "tab-fg"
        self._bind("tT", f"{base}{hint_links} {in_tab}")
        self._bind("tA", f"{base}{hint_all} {in_tab}")

    def _macro(self) -> None:
        self._bind("q", "macro-record")
        self._bind("@", "macro-run")

    def _navigate_tab(self) -> None:
        self._bind(_Util.make_combi("h", decorators="a"), "tab-prev")
        self._bind(_Util.make_combi("l", decorators="a"), "tab-next")
        self._bind(_Util.make_combi("h", decorators="as"), "tab-move -")
        self._bind(_Util.make_combi("l", decorators="as"), "tab-move +")

        self._bind(
            _Util.make_combi("p", decorators="a"), Cmd.enter_as_prompt("tab-give")
        )
        self._bind(
            _Util.make_combi("p", decorators="as"),
            Cmd.enter_as_prompt("tab-give --private"),
        )

        self._bind(_Util.make_combi("tab", decorators="c"), "tab-focus last")
        self._bind(
            _Util.make_combi("`", decorators="a"), Cmd.enter_as_prompt("tab-select")
        )

        cmd_focus = "tab-focus --no-last "  # do NOT switch back on multiple inputs of same index
        for num in range(1, 4):  # [1, 2, 3]
            self._bind(_Util.make_combi(str(num), decorators="a"), f"{cmd_focus}{num}")

        idx_rev = -1
        for num in [0, 9, 8]:
            self._bind(
                _Util.make_combi(str(num), decorators="a"), f"{cmd_focus}{idx_rev}"
            )
            idx_rev -= 1

    def _to_other_modes(self) -> None:
        self._bind(":", "set-cmd-text :")
        self._bind("i", "mode-enter insert")
        self._bind(_Util.make_combi("i", decorators="c"), "hint inputs --first")

        self._bind("v", "mode-enter caret")
        self._bind("V", "mode-enter caret ;; selection-toggle --line")

    def _command(self) -> None:
        self._bind(":", Cmd.enter_as_prompt("", append_space=False))

    def _open(self) -> None:
        self._bind("o", Cmd.enter_as_prompt(Cmd.do_in_new_tab("")))
        self._bind("O", Cmd.enter_as_prompt("open --window"))

        self._bind(_Util.make_combi("r", "c"), "reload --force")

        self._bind(_Util.make_combi("h", "c"), "back")
        self._bind(_Util.make_combi("l", "c"), "forward")

    def _mark(self) -> None:
        self._bind("ba", Cmd.enter_as_prompt("bookmark-add"))
        self._bind("Ba", Cmd.enter_as_prompt("quickmark-add"))

        self._bind("bo", Cmd.enter_as_prompt("bookmark-load --tab"))
        self._bind("Bo", Cmd.enter_as_prompt("quickmark-load --tab"))

    def _gui(self) -> None:
        self._bind("z", "gui_toggle")

        self._bind("Z", Cmd.enter_as_prompt("zoom --quiet 1", append_space=False))

        self._bind(_Util.make_combi("esc"), "jseval -q document.activeElement.blur()")


class ModeCommand(_ModeSpecific):
    def __init__(self, config):
        super().__init__("command", config)

        self._basic()
        self._completion()

    def _basic(self) -> None:
        self._bind(_Util.make_combi("enter"), "command-accept")
        self._bind(_Util.make_combi("enter", decorators="c"), "command-accept --rapid")

    def _completion(self) -> None:
        cmd_completion = "completion-item-focus "
        self._bind(_Util.make_combi("p", decorators="c"), f"{cmd_completion} prev")
        self._bind(_Util.make_combi("n", decorators="c"), f"{cmd_completion} next")
        self._bind(
            _Util.make_combi("tab", decorators="s"), f"{cmd_completion} prev-category"
        )
        self._bind(_Util.make_combi("tab"), f"{cmd_completion} next-category")

        self._bind(_Util.make_combi("k", decorators="c"), "command-history-prev")
        self._bind(_Util.make_combi("j", decorators="c"), "command-history-next")


class ModeInsert(_ModeSpecific):
    def __init__(self, config):
        super().__init__("insert", config)

        self._exit()
        self._edit()

    def _exit(self) -> None:
        # REF:
        #   https://github.com/qutebrowser/qutebrowser/issues/2668
        #   https://stackoverflow.com/questions/2520650/how-do-you-clear-the-focus-in-javascript
        self._bind(
            [_Util.make_combi("esc"), _Util.make_combi("c", decorators="c")],
            Cmd.concat(["mode-leave", "jseval -q document.activeElement.blur()"]),
        )

    def _edit(self) -> None:
        self._bind(_Util.make_combi("e", decorators="c"), "edit-text")


class ModeVisual(_ModeSpecific):
    def __init__(self, config):
        super().__init__("caret", config)

        self._basic()
        self._navigate()
        self._copy()

    def _basic(self) -> None:
        base = "selection-"

        self._bind("v", f"{base}toggle")
        self._bind("V", f"{base}toggle --line")

        self._bind(_Util.make_combi("space"), f"{base}reverse")

    def _navigate(self) -> None:
        base = "move-to-"

        self._bind("h", f"{base}prev-char")
        self._bind("l", f"{base}next-char")
        self._bind("b", f"{base}prev-word")
        self._bind("w", f"{base}next-word")
        self._bind("0", f"{base}start-of-line")
        self._bind("$", f"{base}end-of-line")

        self._bind("k", f"{base}prev-line")
        self._bind("j", f"{base}next-line")
        self._bind("K", Cmd.concat(Cmd.repeat(f"{base}prev-line", 4)))
        self._bind("J", Cmd.concat(Cmd.repeat(f"{base}next-line", 4)))

        self._bind("u", f"{base}start-of-prev-block")
        self._bind("d", f"{base}start-of-next-block")
        self._bind("gg", f"{base}start-of-document")
        self._bind("G", f"{base}end-of-document")

    def _copy(self) -> None:
        base = "yank selection "

        self._bind("y", base)
        self._bind("Y", f"{base}-s")


class ModePrompt(_ModeSpecific):
    def __init__(self, config):
        super().__init__("prompt", config)

        self._basic()

    def _basic(self) -> None:
        self._bind(_Util.make_combi("enter"), "prompt-accept")

        self._bind(_Util.make_combi("tab"), "prompt-item-focus next")
        self._bind(_Util.make_combi("tab", decorators="s"), "prompt-item-focus prev")


class ModePassthrough(_ModeSpecific):
    def __init__(self, config):
        super().__init__("passthrough", config)

        self._exit()

    def _exit(self) -> None:
        self._bind(_Util.make_combi("esc", decorators="s"), "mode-leave")


class Bind:
    def __init__(self, config):
        self._config = config
        self._remove_default()

        self._set_equal_keys()
        self._bind()

    def _remove_default(self) -> None:
        self._config.set("bindings.default", {})

    def _set_equal_keys(self) -> None:
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

    def _bind(self) -> None:
        ModeMulti(self._config)

        ModeNormal(self._config)
        ModeCommand(self._config)
        ModeInsert(self._config)
        ModeVisual(self._config)
        ModePrompt(self._config)
        ModePassthrough(self._config)
