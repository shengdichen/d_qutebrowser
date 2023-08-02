class Visual:
    def __init__(self, config):
        self._config = config

        self._palette = {
            "background": "#282a36",
            "background-alt": "#282a36",
            "background-attention": "#181920",
            "border": "#282a36",
            "current-line": "#44475a",
            "selection": "#44475a",
            "foreground": "#f8f8f2",
            "foreground-alt": "#e0e0e0",
            "foreground-attention": "#ffffff",
            "comment": "#6272a4",
            "cyan": "#8be9fd",
            "green": "#50fa7b",
            "orange": "#ffb86c",
            "pink": "#ff79c6",
            "purple": "#bd93f9",
            "red": "#ff5555",
            "yellow": "#f1fa8c",
        }
        self._palette_ours = {
            "black": "#000000",
            "grey_dark": "#352c37",
            "grey_bright": "#897397",
            "white": "#ede3f7",
            "red": "#ef3347",
            "pink": "#ff79c6",
            "magenta": "#bd93f9",
            "cyan": "#8be9fd",
        }

        spacing = {"vertical": 6, "horizontal": 8}
        self._padding = {
            "top": spacing["vertical"],
            "right": spacing["horizontal"],
            "bottom": spacing["vertical"],
            "left": spacing["horizontal"],
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

        self._config.set(base + "even.bg", self._palette_ours["black"])
        self._config.set(base + "odd.bg", self._palette_ours["black"])
        self._config.set(base + "fg", self._palette_ours["white"])
        self._config.set(base + "match.fg", self._palette_ours["pink"])

        self._config.set(base + "category.bg", self._palette_ours["black"])
        self._config.set(base + "category.fg", self._palette_ours["white"])
        for specification in ["bottom", "top"]:
            self._config.set(
                ".".join([base + "category.border", specification]),
                self._palette_ours["grey_bright"],
            )

        self._config.set(base + "item.selected.bg", self._palette_ours["grey_dark"])
        self._config.set(base + "item.selected.fg", self._palette_ours["white"])
        for specification in ["bottom", "top"]:
            self._config.set(
                ".".join([base + "item.selected.border", specification]),
                self._palette_ours["white"],
            )

        self._config.set(base + "scrollbar.bg", self._palette_ours["black"])
        self._config.set(base + "scrollbar.fg", self._palette_ours["grey_dark"])

    def _set_downloads(self) -> None:
        base = "colors.downloads."

        # disable gradient
        self._config.set(base + "system.bg", "none")
        self._config.set(base + "system.fg", "none")

        for item in ["bar", "start", "stop"]:
            self._config.set(f"{base}{item}.bg", self._palette_ours["black"])
        for item in ["start", "stop"]:
            self._config.set(f"{base}{item}.fg", self._palette_ours["white"])

        self._config.set(base + "error.bg", self._palette_ours["black"])
        self._config.set(base + "error.fg", self._palette_ours["red"])

    def _set_hints(self) -> None:
        base = "hints."
        self._config.set(f"{base}radius", 0)
        self._config.set(f"{base}scatter", True)  # scatter chars used for hinting
        self._config.set(
            f"{base}padding", {"top": 1, "bottom": 1, "left": 3, "right": 3}
        )
        self._config.set(
            f"{base}border", f"1.7px solid {self._palette_ours['grey_dark']}"
        )

        base = "colors.hints."
        self._config.set(f"{base}bg", self._palette_ours["black"])
        self._config.set(f"{base}fg", self._palette_ours["magenta"])
        self._config.set(f"{base}match.fg", self._palette_ours["white"])

    def _set_keyhint(self) -> None:
        base = "colors.keyhint."
        self._config.set("keyhint.radius", 0)

        self._config.set(f"{base}bg", self._palette_ours["black"])
        self._config.set(f"{base}fg", self._palette_ours["white"])
        self._config.set(f"{base}suffix.fg", self._palette_ours["magenta"])

    def _set_messages(self) -> None:
        self._config.set("colors.messages.info.bg", self._palette_ours["black"])
        self._config.set("colors.messages.info.border", self._palette_ours["black"])
        self._config.set("colors.messages.info.fg", self._palette_ours["white"])

        self._config.set("colors.messages.warning.bg", self._palette_ours["black"])
        self._config.set("colors.messages.warning.border", self._palette_ours["red"])
        self._config.set("colors.messages.warning.fg", self._palette_ours["white"])

        self._config.set("colors.messages.error.bg", self._palette_ours["black"])
        self._config.set("colors.messages.error.border", self._palette_ours["black"])
        self._config.set("colors.messages.error.fg", self._palette_ours["red"])

    def _set_prompts(self) -> None:
        base = "colors.prompts."
        self._config.set("prompt.radius", 0)

        self._config.set(base + "bg", self._palette_ours["black"])
        self._config.set(base + "fg", self._palette_ours["white"])
        self._config.set(base + "selected.bg", self._palette_ours["grey_dark"])
        self._config.set(base + "selected.fg", self._palette_ours["white"])
        self._config.set(base + "border", "1px solid " + self._palette_ours["white"])

    def _set_statusbar(self) -> None:
        self._config.set("statusbar.show", "always")
        self._config.set("statusbar.position", "bottom")
        # default: ["keypress", "url", "scroll", "history", "tabs", "progress"]
        self._config.set("statusbar.widgets", ["keypress", "url"])

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
            self._config.set(base + mode + ".bg", self._palette_ours["black"])
            self._config.set(base + mode + ".fg", self._palette_ours["white"])

        self._config.set(base + "progress.bg", self._palette_ours["grey_bright"])

        self._config.set(base + "url.fg", self._palette_ours["white"])
        self._config.set(base + "url.success.http.fg", self._palette_ours["white"])
        self._config.set(base + "url.success.https.fg", self._palette_ours["white"])

        self._config.set(base + "url.hover.fg", self._palette_ours["cyan"])
        self._config.set(base + "url.warn.fg", self._palette_ours["red"])
        self._config.set(base + "url.error.fg", self._palette_ours["red"])

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
                ".".join([item_base, specification, "bg"]), self._palette_ours["black"]
            )
        for specification in ["even", "odd"]:
            self._config.set(
                ".".join([item_base, specification, "fg"]),
                self._palette_ours["grey_bright"],
            )

        for specification in ["even", "odd"]:
            self._config.set(
                ".".join([item_base, "selected", specification, "bg"]),
                self._palette_ours["black"],
            )
        for specification in ["even", "odd"]:
            self._config.set(
                ".".join([item_base, "selected", specification, "fg"]),
                self._palette_ours["white"],
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
