import typing


class _Util:
    palette = {
        "black": "#000000",
        "grey_dark": "#352c37",
        "grey_bright": "#897397",
        "white": "#ede3f7",
        "red": "#ef3347",
        "pink": "#ff79c6",
        "magenta": "#bd93f9",
        "cyan": "#8be9fd",
    }

    fonts = {
        "shevska": "Shevska",
        "avenir": "Avenir LT Std",
        "constantia": "Constantia",
    }


class _VisualItem:
    def __init__(self, config):
        self._config = config

    def _set(self, key: str, value: typing.Any) -> None:
        self._config.set(key, value)


class Completion(_VisualItem):
    def apply(self) -> None:
        base = "colors.completion."

        self._set(f"{base}even.bg", _Util.palette["black"])
        self._set(f"{base}odd.bg", _Util.palette["black"])
        self._set(f"{base}fg", _Util.palette["white"])
        self._set(f"{base}match.fg", _Util.palette["pink"])

        self._set(f"{base}category.bg", _Util.palette["black"])
        self._set(f"{base}category.fg", _Util.palette["white"])
        for specification in ["bottom", "top"]:
            self._set(
                ".".join([f"{base}category.border", specification]),
                _Util.palette["grey_bright"],
            )

        self._set(f"{base}item.selected.bg", _Util.palette["grey_dark"])
        self._set(f"{base}item.selected.fg", _Util.palette["white"])
        for specification in ["bottom", "top"]:
            self._set(
                ".".join([f"{base}item.selected.border", specification]),
                _Util.palette["white"],
            )

        self._set(f"{base}scrollbar.bg", _Util.palette["black"])
        self._set(f"{base}scrollbar.fg", _Util.palette["grey_dark"])


class Download(_VisualItem):
    def apply(self) -> None:
        base = "colors.downloads."

        # disable gradient
        self._set(f"{base}system.bg", "none")
        self._set(f"{base}system.fg", "none")

        for item in ["bar", "start", "stop"]:
            self._set(f"{base}{item}.bg", _Util.palette["black"])
        for item in ["start", "stop"]:
            self._set(f"{base}{item}.fg", _Util.palette["white"])

        self._set(f"{base}error.bg", _Util.palette["black"])
        self._set(f"{base}error.fg", _Util.palette["red"])


class Hint(_VisualItem):
    def apply(self) -> None:
        base = "hints."
        self._set(f"{base}radius", 0)
        self._set(f"{base}scatter", True)  # scatter chars used for hinting
        self._set(f"{base}padding", {"top": 1, "bottom": 1, "left": 3, "right": 3})
        self._set(f"{base}border", f"1.7px solid {_Util.palette['grey_dark']}")

        base = "colors.hints."
        self._set(f"{base}bg", _Util.palette["black"])
        self._set(f"{base}fg", _Util.palette["magenta"])
        self._set(f"{base}match.fg", _Util.palette["white"])


class Keyhint(_VisualItem):
    def apply(self) -> None:
        base = "colors.keyhint."
        self._set("keyhint.radius", 0)

        self._set(f"{base}bg", _Util.palette["black"])
        self._set(f"{base}fg", _Util.palette["white"])
        self._set(f"{base}suffix.fg", _Util.palette["magenta"])


class Message(_VisualItem):
    def apply(self) -> None:
        base = "colors.messages."

        self._set(f"{base}info.bg", _Util.palette["black"])
        self._set(f"{base}info.border", _Util.palette["black"])
        self._set(f"{base}info.fg", _Util.palette["white"])

        self._set(f"{base}warning.bg", _Util.palette["black"])
        self._set(f"{base}warning.border", _Util.palette["red"])
        self._set(f"{base}warning.fg", _Util.palette["white"])

        self._set(f"{base}error.bg", _Util.palette["black"])
        self._set(f"{base}error.border", _Util.palette["black"])
        self._set(f"{base}error.fg", _Util.palette["red"])


class Prompt(_VisualItem):
    def apply(self) -> None:
        base = "colors.prompts."
        self._set("prompt.radius", 0)

        self._set(f"{base}bg", _Util.palette["black"])
        self._set(f"{base}fg", _Util.palette["white"])
        self._set(f"{base}selected.bg", _Util.palette["grey_dark"])
        self._set(f"{base}selected.fg", _Util.palette["white"])
        self._set(f"{base}border", f"1px solid {_Util.palette['white']}")


class Tab(_VisualItem):
    def apply(self) -> None:
        self._set("tabs.show", "always")
        self._set("tabs.position", "bottom")
        self._set("tabs.title.alignment", "center")
        self._set("tabs.title.format", "{perc}{index}/{current_title}")
        self._set(
            "tabs.padding",
            {"top": 1, "bottom": 0, "left": 2, "right": 2},
        )

        self._set("tabs.favicons.show", "never")
        self._set("tabs.indicator.width", 0)  # disable completely

        item_base = "colors.tabs"

        for specification in ["bar", "even", "odd"]:
            self._set(
                ".".join([item_base, specification, "bg"]), _Util.palette["black"]
            )
        for specification in ["even", "odd"]:
            self._set(
                ".".join([item_base, specification, "fg"]),
                _Util.palette["grey_bright"],
            )

        for specification in ["even", "odd"]:
            self._set(
                ".".join([item_base, "selected", specification, "bg"]),
                _Util.palette["black"],
            )
        for specification in ["even", "odd"]:
            self._set(
                ".".join([item_base, "selected", specification, "fg"]),
                _Util.palette["white"],
            )


class Statusbar(_VisualItem):
    def apply(self) -> None:
        base = "statusbar."
        self._set(f"{base}show", "always")
        self._set(f"{base}position", "bottom")
        # default: ["keypress", "url", "scroll", "history", "tabs", "progress"]
        self._set(f"{base}widgets", ["keypress", "url"])

        base = "colors.statusbar."

        for mode in [
            "normal",
            "private",
            "insert",
            "command",
            "command.private",
            "caret",
            "caret.selection",
            "passthrough",
        ]:
            self._set(f"{base}{mode}.bg", _Util.palette["black"])
            self._set(f"{base}{mode}.fg", _Util.palette["white"])

        self._set(f"{base}progress.bg", _Util.palette["grey_bright"])

        self._set(f"{base}url.fg", _Util.palette["white"])
        self._set(f"{base}url.success.http.fg", _Util.palette["white"])
        self._set(f"{base}url.success.https.fg", _Util.palette["white"])

        self._set(f"{base}url.hover.fg", _Util.palette["cyan"])
        self._set(f"{base}url.warn.fg", _Util.palette["red"])
        self._set(f"{base}url.error.fg", _Util.palette["red"])

        self._set(
            "statusbar.padding",
            {"top": 0, "bottom": 0, "left": 2, "right": 2},
        )


class Font(_VisualItem):
    def __init__(self, config):
        super().__init__(config)

        self._config_base = "fonts."
        self._monospace = _Util.fonts["shevska"]
        self._sans = _Util.fonts["avenir"]
        self._serif = _Util.fonts["constantia"]

    def apply(self, disable_remote: bool = False) -> None:
        if disable_remote:
            self._disable_remote()

        self._set_default_family()
        self._set_ui()
        self._set_web()

    def _disable_remote(self) -> None:
        # might be problematic due to:
        #   1. missing glyph in our font
        #   2. some sites will still use their font(s)
        self._config.get("qt.args").append("disable-remote-fonts")

    def _set_default_family(self) -> None:
        self._config.set(f"{self._config_base}default_family", self._monospace)
        self._config.set(f"{self._config_base}default_size", "11pt")

    def _set_ui(self) -> None:
        for item, size in zip(["hints", "statusbar", "prompts"], [14, 14, 13]):
            self._use_default_family(item, size)

    def _use_default_family(self, item: str, size: int) -> None:
        self._config.set(f"{self._config_base}{item}", f"{size}pt default_family")

    def _set_web(self) -> None:
        base = f"{self._config_base}web."

        base_family = f"{base}family."
        self._config.set(f"{base_family}fixed", self._monospace)
        for specification in ["standard", "sans_serif", "cursive", "fantasy"]:
            self._config.set(f"{base_family}{specification}", self._sans)
        for specification in ["serif"]:
            self._config.set(f"{base_family}{specification}", self._serif)

        base_size = f"{base}size."
        # common default (also seen in firefox)
        self._config.set(f"{base_size}default", 16)
        self._config.set(f"{base_size}default_fixed", 13)


class Visual:
    def __init__(self, config):
        self._config = config

    def apply(self) -> None:
        self._set_general()
        self._set_window()
        self._set_components()

        Font(self._config).apply()

    def _set_general(self) -> None:
        self._config.set("colors.webpage.preferred_color_scheme", "dark")
        self._config.set("colors.webpage.darkmode.enabled", True)

    def _set_window(self) -> None:
        self._config.set("window.hide_decoration", True)
        self._config.set("window.title_format", "{private}{current_title}")

        self._config.set("zoom.default", "127%")

        levels = [f"{int(100 * (1.07 ** power))}%" for power in range(-9, +10)]
        self._config.set("zoom.levels", levels)

    def _set_components(self) -> None:
        Completion(self._config).apply()
        Download(self._config).apply()
        Hint(self._config).apply()
        Keyhint(self._config).apply()
        Message(self._config).apply()
        Prompt(self._config).apply()
        Statusbar(self._config).apply()
        Tab(self._config).apply()
