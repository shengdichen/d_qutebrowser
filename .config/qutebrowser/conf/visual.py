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
        # Background color of the completion widget category headers.
        self._config.set("colors.completion.category.bg", self._palette["background"])

        # Bottom border color of the completion widget category headers.
        self._config.set(
            "colors.completion.category.border.bottom", self._palette["border"]
        )

        # Top border color of the completion widget category headers.
        self._config.set(
            "colors.completion.category.border.top", self._palette["border"]
        )

        # Foreground color of completion widget category headers.
        self._config.set("colors.completion.category.fg", self._palette["foreground"])

        # Background color of the completion widget for even rows.
        self._config.set("colors.completion.even.bg", self._palette["background"])

        # Background color of the completion widget for odd rows.
        self._config.set("colors.completion.odd.bg", self._palette["background-alt"])

        # Text color of the completion widget.
        self._config.set("colors.completion.fg", self._palette["foreground"])

        # Background color of the selected completion item.
        self._config.set(
            "colors.completion.item.selected.bg", self._palette["selection"]
        )

        # Bottom border color of the selected completion item.
        self._config.set(
            "colors.completion.item.selected.border.bottom", self._palette["selection"]
        )

        # Top border color of the completion widget category headers.
        self._config.set(
            "colors.completion.item.selected.border.top", self._palette["selection"]
        )

        # Foreground color of the selected completion item.
        self._config.set(
            "colors.completion.item.selected.fg", self._palette["foreground"]
        )

        # Foreground color of the matched text in the completion.
        self._config.set("colors.completion.match.fg", self._palette["orange"])

        # Color of the scrollbar in completion view
        self._config.set("colors.completion.scrollbar.bg", self._palette["background"])

        # Color of the scrollbar handle in completion view.
        self._config.set("colors.completion.scrollbar.fg", self._palette["foreground"])

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
        # Background color for hints. Note that you can use a `rgba(...)` value
        # for transparency.
        self._config.set("colors.hints.bg", self._palette["background"])

        # Font color for hints.
        self._config.set("colors.hints.fg", self._palette["purple"])

        # Hints
        self._config.set("hints.border", "1px solid " + self._palette["background-alt"])

        # Font color for the matched part of hints.
        self._config.set("colors.hints.match.fg", self._palette["foreground-alt"])

        # Background color of the keyhint widget.
        self._config.set("colors.keyhint.bg", self._palette["background"])

        # Text color for the keyhint widget.
        self._config.set("colors.keyhint.fg", self._palette["purple"])

        # Highlight color for keys to complete the current keychain.
        self._config.set("colors.keyhint.suffix.fg", self._palette["selection"])

    def _set_messages(self) -> None:
        # Background color of an error message.
        self._config.set("colors.messages.error.bg", self._palette["background"])

        # Border color of an error message.
        self._config.set(
            "colors.messages.error.border", self._palette["background-alt"]
        )

        # Foreground color of an error message.
        self._config.set("colors.messages.error.fg", self._palette["red"])

        # Background color of an info message.
        self._config.set("colors.messages.info.bg", self._palette["background"])

        # Border color of an info message.
        self._config.set("colors.messages.info.border", self._palette["background-alt"])

        # Foreground color an info message.
        self._config.set("colors.messages.info.fg", self._palette["comment"])

        # Background color of a warning message.
        self._config.set("colors.messages.warning.bg", self._palette["background"])

        # Border color of a warning message.
        self._config.set(
            "colors.messages.warning.border", self._palette["background-alt"]
        )

        # Foreground color a warning message.
        self._config.set("colors.messages.warning.fg", self._palette["red"])

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

        # Background color of the statusbar in caret mode.
        self._config.set("colors.statusbar.caret.bg", self._palette["background"])

        # Foreground color of the statusbar in caret mode.
        self._config.set("colors.statusbar.caret.fg", self._palette["orange"])

        # Background color of the statusbar in caret mode with a selection.
        self._config.set(
            "colors.statusbar.caret.selection.bg", self._palette["background"]
        )

        # Foreground color of the statusbar in caret mode with a selection.
        self._config.set("colors.statusbar.caret.selection.fg", self._palette["orange"])

        # Background color of the statusbar in command mode.
        self._config.set("colors.statusbar.command.bg", self._palette["background"])

        # Foreground color of the statusbar in command mode.
        self._config.set("colors.statusbar.command.fg", self._palette["pink"])

        # Background color of the statusbar in private browsing + command mode.
        self._config.set(
            "colors.statusbar.command.private.bg", self._palette["background"]
        )

        # Foreground color of the statusbar in private browsing + command mode.
        self._config.set(
            "colors.statusbar.command.private.fg", self._palette["foreground-alt"]
        )

        # Background color of the statusbar in insert mode.
        self._config.set(
            "colors.statusbar.insert.bg", self._palette["background-attention"]
        )

        # Foreground color of the statusbar in insert mode.
        self._config.set(
            "colors.statusbar.insert.fg", self._palette["foreground-attention"]
        )

        # Background color of the statusbar.
        self._config.set("colors.statusbar.normal.bg", self._palette["background"])

        # Foreground color of the statusbar.
        self._config.set("colors.statusbar.normal.fg", self._palette["foreground"])

        # Background color of the statusbar in passthrough mode.
        self._config.set("colors.statusbar.passthrough.bg", self._palette["background"])

        # Foreground color of the statusbar in passthrough mode.
        self._config.set("colors.statusbar.passthrough.fg", self._palette["orange"])

        # Background color of the statusbar in private browsing mode.
        self._config.set("colors.statusbar.private.bg", self._palette["background-alt"])

        # Foreground color of the statusbar in private browsing mode.
        self._config.set("colors.statusbar.private.fg", self._palette["foreground-alt"])

        # Background color of the progress bar.
        self._config.set("colors.statusbar.progress.bg", self._palette["background"])

        # Foreground color of the URL in the statusbar on error.
        self._config.set("colors.statusbar.url.error.fg", self._palette["red"])

        # Default foreground color of the URL in the statusbar.
        self._config.set("colors.statusbar.url.fg", self._palette["foreground"])

        # Foreground color of the URL in the statusbar for hovered links.
        self._config.set("colors.statusbar.url.hover.fg", self._palette["cyan"])

        # Foreground color of the URL in the statusbar on successful load
        self._config.set("colors.statusbar.url.success.http.fg", self._palette["green"])

        # Foreground color of the URL in the statusbar on successful load
        self._config.set(
            "colors.statusbar.url.success.https.fg", self._palette["green"]
        )

        # Foreground color of the URL in the statusbar when there's a warning.
        self._config.set("colors.statusbar.url.warn.fg", self._palette["yellow"])

        # Status bar padding
        self._config.set("statusbar.padding", self._padding)

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
