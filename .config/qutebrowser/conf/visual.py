class Visual:
    def __init__(self, config):
        self._config = config

        self._palette = {
            "black": "#000000",
            "grey_dark": "#352c37",
            "grey_bright": "#897397",
            "white": "#ede3f7",
            "red": "#ef3347",
            "pink": "#ff79c6",
            "magenta": "#bd93f9",
            "cyan": "#8be9fd",
        }

    def apply(self) -> None:
        self._set_colorscheme()
        self._set_font()
        self._set_window()

        self._config.set("colors.webpage.preferred_color_scheme", "dark")
        self._config.set("colors.webpage.darkmode.enabled", True)

    def _set_colorscheme(self) -> None:
        self._set_completion()
        self._set_downloads()
        self._set_hints()
        self._set_keyhint()
        self._set_messages()
        self._set_prompts()
        self._set_statusbar()
        self._set_tabs()

    def _set_completion(self) -> None:
        base = "colors.completion."

        self._config.set(f"{base}even.bg", self._palette["black"])
        self._config.set(f"{base}odd.bg", self._palette["black"])
        self._config.set(f"{base}fg", self._palette["white"])
        self._config.set(f"{base}match.fg", self._palette["pink"])

        self._config.set(f"{base}category.bg", self._palette["black"])
        self._config.set(f"{base}category.fg", self._palette["white"])
        for specification in ["bottom", "top"]:
            self._config.set(
                ".".join([f"{base}category.border", specification]),
                self._palette["grey_bright"],
            )

        self._config.set(f"{base}item.selected.bg", self._palette["grey_dark"])
        self._config.set(f"{base}item.selected.fg", self._palette["white"])
        for specification in ["bottom", "top"]:
            self._config.set(
                ".".join([f"{base}item.selected.border", specification]),
                self._palette["white"],
            )

        self._config.set(f"{base}scrollbar.bg", self._palette["black"])
        self._config.set(f"{base}scrollbar.fg", self._palette["grey_dark"])

    def _set_downloads(self) -> None:
        base = "colors.downloads."

        # disable gradient
        self._config.set(f"{base}system.bg", "none")
        self._config.set(f"{base}system.fg", "none")

        for item in ["bar", "start", "stop"]:
            self._config.set(f"{base}{item}.bg", self._palette["black"])
        for item in ["start", "stop"]:
            self._config.set(f"{base}{item}.fg", self._palette["white"])

        self._config.set(f"{base}error.bg", self._palette["black"])
        self._config.set(f"{base}error.fg", self._palette["red"])

    def _set_hints(self) -> None:
        base = "hints."
        self._config.set(f"{base}radius", 0)
        self._config.set(f"{base}scatter", True)  # scatter chars used for hinting
        self._config.set(
            f"{base}padding", {"top": 1, "bottom": 1, "left": 3, "right": 3}
        )
        self._config.set(f"{base}border", f"1.7px solid {self._palette['grey_dark']}")

        base = "colors.hints."
        self._config.set(f"{base}bg", self._palette["black"])
        self._config.set(f"{base}fg", self._palette["magenta"])
        self._config.set(f"{base}match.fg", self._palette["white"])

    def _set_keyhint(self) -> None:
        base = "colors.keyhint."
        self._config.set("keyhint.radius", 0)

        self._config.set(f"{base}bg", self._palette["black"])
        self._config.set(f"{base}fg", self._palette["white"])
        self._config.set(f"{base}suffix.fg", self._palette["magenta"])

    def _set_messages(self) -> None:
        base = "colors.messages."

        self._config.set(f"{base}info.bg", self._palette["black"])
        self._config.set(f"{base}info.border", self._palette["black"])
        self._config.set(f"{base}info.fg", self._palette["white"])

        self._config.set(f"{base}warning.bg", self._palette["black"])
        self._config.set(f"{base}warning.border", self._palette["red"])
        self._config.set(f"{base}warning.fg", self._palette["white"])

        self._config.set(f"{base}error.bg", self._palette["black"])
        self._config.set(f"{base}error.border", self._palette["black"])
        self._config.set(f"{base}error.fg", self._palette["red"])

    def _set_prompts(self) -> None:
        base = "colors.prompts."
        self._config.set("prompt.radius", 0)

        self._config.set(f"{base}bg", self._palette["black"])
        self._config.set(f"{base}fg", self._palette["white"])
        self._config.set(f"{base}selected.bg", self._palette["grey_dark"])
        self._config.set(f"{base}selected.fg", self._palette["white"])
        self._config.set(f"{base}border", f"1px solid {self._palette['white']}")

    def _set_statusbar(self) -> None:
        base = "statusbar."
        self._config.set(f"{base}show", "always")
        self._config.set(f"{base}position", "bottom")
        # default: ["keypress", "url", "scroll", "history", "tabs", "progress"]
        self._config.set(f"{base}widgets", ["keypress", "url"])

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
            self._config.set(f"{base}{mode}.bg", self._palette["black"])
            self._config.set(f"{base}{mode}.fg", self._palette["white"])

        self._config.set(f"{base}progress.bg", self._palette["grey_bright"])

        self._config.set(f"{base}url.fg", self._palette["white"])
        self._config.set(f"{base}url.success.http.fg", self._palette["white"])
        self._config.set(f"{base}url.success.https.fg", self._palette["white"])

        self._config.set(f"{base}url.hover.fg", self._palette["cyan"])
        self._config.set(f"{base}url.warn.fg", self._palette["red"])
        self._config.set(f"{base}url.error.fg", self._palette["red"])

        self._config.set(
            "statusbar.padding",
            {"top": 0, "bottom": 0, "left": 2, "right": 2},
        )

    def _set_tabs(self) -> None:
        self._config.set("tabs.show", "always")
        self._config.set("tabs.position", "bottom")
        self._config.set("tabs.title.alignment", "center")
        self._config.set("tabs.title.format", "{perc}{index}/{current_title}")
        self._config.set(
            "tabs.padding",
            {"top": 1, "bottom": 0, "left": 2, "right": 2},
        )

        self._config.set("tabs.favicons.show", "never")
        self._config.set("tabs.indicator.width", 0)  # disable completely

        item_base = "colors.tabs"

        for specification in ["bar", "even", "odd"]:
            self._config.set(
                ".".join([item_base, specification, "bg"]), self._palette["black"]
            )
        for specification in ["even", "odd"]:
            self._config.set(
                ".".join([item_base, specification, "fg"]),
                self._palette["grey_bright"],
            )

        for specification in ["even", "odd"]:
            self._config.set(
                ".".join([item_base, "selected", specification, "bg"]),
                self._palette["black"],
            )
        for specification in ["even", "odd"]:
            self._config.set(
                ".".join([item_base, "selected", specification, "fg"]),
                self._palette["white"],
            )

    def _set_font(self) -> None:
        fonts = {
            "shevska": "Shevska",
            "avenir": "Avenir LT Std",
            "constantia": "Constantia",
        }

        base = "fonts"
        for specification in ["default_family", "web.family.fixed"]:
            self._config.set(".".join([base, specification]), fonts["shevska"])
        self._config.set("fonts.default_size", "11pt")
        self._config.set("fonts.hints", "14pt default_family")
        self._config.set("fonts.statusbar", "14pt default_family")
        self._config.set("fonts.prompts", "13pt default_family")

        # do our best at using our font (some sites will still use their theirs)
        self._config.get("qt.args").append("disable-remote-fonts")
        for specification in ["standard", "sans_serif", "cursive", "fantasy"]:
            self._config.set(
                ".".join([base, "web", "family", specification]), fonts["avenir"]
            )
        for specification in ["serif"]:
            self._config.set(
                ".".join([base, "web", "family", specification]), fonts["constantia"]
            )

        # common default (also seen in firefox)
        self._config.set("fonts.web.size.default", 16)
        self._config.set("fonts.web.size.default_fixed", 13)

    def _set_window(self) -> None:
        self._config.set("window.hide_decoration", True)
        self._config.set("window.title_format", "{current_title}")

        self._config.set("zoom.default", "123%")
