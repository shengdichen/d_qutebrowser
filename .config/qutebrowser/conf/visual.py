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

        self._config.set("colors.webpage.preferred_color_scheme", "dark")
        self._config.set("colors.webpage.darkmode.enabled", True)

    def _set_colorscheme(self) -> None:
        self._set_completion()
        self._set_downloads()
        self._set_hints()
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
        # Background color for the download bar.
        self._config.set("colors.downloads.bar.bg", self._palette["background"])

        # Background color for downloads with errors.
        self._config.set("colors.downloads.error.bg", self._palette["background"])

        # Foreground color for downloads with errors.
        self._config.set("colors.downloads.error.fg", self._palette["red"])

        # Color gradient stop for download backgrounds.
        self._config.set("colors.downloads.stop.bg", self._palette["background"])

        # Color gradient interpolation system for download backgrounds.
        # Type: ColorSystem
        # Valid values:
        #   - rgb: Interpolate in the RGB color system.
        #   - hsv: Interpolate in the HSV color system.
        #   - hsl: Interpolate in the HSL color system.
        #   - none: Don't show a gradient.
        self._config.set("colors.downloads.system.bg", "none")

    def _set_hints(self) -> None:
        self._config.set("colors.hints.bg", self._palette_ours["black"])
        # slight hack to increase the area of background
        self._config.set("hints.border", "3.7px solid " + self._palette_ours["black"])
        self._config.set("colors.hints.fg", self._palette_ours["magenta"])
        self._config.set("colors.hints.match.fg", self._palette_ours["white"])

        self._config.set("colors.keyhint.bg", self._palette_ours["black"])
        self._config.set("colors.keyhint.fg", self._palette_ours["white"])
        self._config.set("colors.keyhint.suffix.fg", self._palette_ours["magenta"])

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
        # Background color for prompts.
        self._config.set("colors.prompts.bg", self._palette["background"])

        #  Border used around UI elements in prompts.
        self._config.set(
            "colors.prompts.border", "1px solid " + self._palette["background-alt"]
        )

        # Foreground color for prompts.
        self._config.set("colors.prompts.fg", self._palette["cyan"])

        # Background color for the selected item in filename prompts.
        self._config.set("colors.prompts.selected.bg", self._palette["selection"])

    def _set_statusbar(self) -> None:
        self._config.set("statusbar.show", "in-mode")

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
            {"top": 1, "bottom": 1, "left": 2, "right": 2},
        )

    def _set_tabs(self) -> None:
        self._config.set(
            "tabs.show", "multiple"
        )  # only show if multiple tabs are present
        self._config.set("tabs.position", "left")
        self._config.set("tabs.width", "11%")
        self._config.set("tabs.title.alignment", "left")

        self._config.set("tabs.favicons.show", "never")
        self._config.set("tabs.title.format", "{current_title}")
        self._config.set(
            "tabs.padding",
            {"top": 0, "bottom": 5, "left": 2, "right": 5},
        )
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
        self._config.set("fonts.hints", "14pt Shevska")
        self._config.set("fonts.statusbar", "17pt Shevska")

        for specification in ["standard", "sans_serif", "cursive", "fantasy"]:
            self._config.set(
                ".".join([base, "web", "family", specification]), fonts["avenir"]
            )
        for specification in ["serif"]:
            self._config.set(
                ".".join([base, "web", "family", specification]), fonts["constantia"]
            )

        self._config.set("fonts.web.size.default", 19)
        self._config.set("fonts.web.size.default_fixed", 15)
