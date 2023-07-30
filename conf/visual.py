class Visual:
    def __init__(self):
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

        spacing = {"vertical": 6, "horizontal": 8}
        self._padding = {
            "top": spacing["vertical"],
            "right": spacing["horizontal"],
            "bottom": spacing["vertical"],
            "left": spacing["horizontal"],
        }

    def apply(self, c) -> None:
        # Background color of the completion widget category headers.
        c.colors.completion.category.bg = self._palette["background"]

        # Bottom border color of the completion widget category headers.
        c.colors.completion.category.border.bottom = self._palette["border"]

        # Top border color of the completion widget category headers.
        c.colors.completion.category.border.top = self._palette["border"]

        # Foreground color of completion widget category headers.
        c.colors.completion.category.fg = self._palette["foreground"]

        # Background color of the completion widget for even rows.
        c.colors.completion.even.bg = self._palette["background"]

        # Background color of the completion widget for odd rows.
        c.colors.completion.odd.bg = self._palette["background-alt"]

        # Text color of the completion widget.
        c.colors.completion.fg = self._palette["foreground"]

        # Background color of the selected completion item.
        c.colors.completion.item.selected.bg = self._palette["selection"]

        # Bottom border color of the selected completion item.
        c.colors.completion.item.selected.border.bottom = self._palette["selection"]

        # Top border color of the completion widget category headers.
        c.colors.completion.item.selected.border.top = self._palette["selection"]

        # Foreground color of the selected completion item.
        c.colors.completion.item.selected.fg = self._palette["foreground"]

        # Foreground color of the matched text in the completion.
        c.colors.completion.match.fg = self._palette["orange"]

        # Color of the scrollbar in completion view
        c.colors.completion.scrollbar.bg = self._palette["background"]

        # Color of the scrollbar handle in completion view.
        c.colors.completion.scrollbar.fg = self._palette["foreground"]

        # Background color for the download bar.
        c.colors.downloads.bar.bg = self._palette["background"]

        # Background color for downloads with errors.
        c.colors.downloads.error.bg = self._palette["background"]

        # Foreground color for downloads with errors.
        c.colors.downloads.error.fg = self._palette["red"]

        # Color gradient stop for download backgrounds.
        c.colors.downloads.stop.bg = self._palette["background"]

        # Color gradient interpolation system for download backgrounds.
        # Type: ColorSystem
        # Valid values:
        #   - rgb: Interpolate in the RGB color system.
        #   - hsv: Interpolate in the HSV color system.
        #   - hsl: Interpolate in the HSL color system.
        #   - none: Don't show a gradient.
        c.colors.downloads.system.bg = "none"

        # Background color for hints. Note that you can use a `rgba(...)` value
        # for transparency.
        c.colors.hints.bg = self._palette["background"]

        # Font color for hints.
        c.colors.hints.fg = self._palette["purple"]

        # Hints
        c.hints.border = "1px solid " + self._palette["background-alt"]

        # Font color for the matched part of hints.
        c.colors.hints.match.fg = self._palette["foreground-alt"]

        # Background color of the keyhint widget.
        c.colors.keyhint.bg = self._palette["background"]

        # Text color for the keyhint widget.
        c.colors.keyhint.fg = self._palette["purple"]

        # Highlight color for keys to complete the current keychain.
        c.colors.keyhint.suffix.fg = self._palette["selection"]

        # Background color of an error message.
        c.colors.messages.error.bg = self._palette["background"]

        # Border color of an error message.
        c.colors.messages.error.border = self._palette["background-alt"]

        # Foreground color of an error message.
        c.colors.messages.error.fg = self._palette["red"]

        # Background color of an info message.
        c.colors.messages.info.bg = self._palette["background"]

        # Border color of an info message.
        c.colors.messages.info.border = self._palette["background-alt"]

        # Foreground color an info message.
        c.colors.messages.info.fg = self._palette["comment"]

        # Background color of a warning message.
        c.colors.messages.warning.bg = self._palette["background"]

        # Border color of a warning message.
        c.colors.messages.warning.border = self._palette["background-alt"]

        # Foreground color a warning message.
        c.colors.messages.warning.fg = self._palette["red"]

        # Background color for prompts.
        c.colors.prompts.bg = self._palette["background"]

        #  Border used around UI elements in prompts.
        c.colors.prompts.border = "1px solid " + self._palette["background-alt"]

        # Foreground color for prompts.
        c.colors.prompts.fg = self._palette["cyan"]

        # Background color for the selected item in filename prompts.
        c.colors.prompts.selected.bg = self._palette["selection"]

        # Background color of the statusbar in caret mode.
        c.colors.statusbar.caret.bg = self._palette["background"]

        # Foreground color of the statusbar in caret mode.
        c.colors.statusbar.caret.fg = self._palette["orange"]

        # Background color of the statusbar in caret mode with a selection.
        c.colors.statusbar.caret.selection.bg = self._palette["background"]

        # Foreground color of the statusbar in caret mode with a selection.
        c.colors.statusbar.caret.selection.fg = self._palette["orange"]

        # Background color of the statusbar in command mode.
        c.colors.statusbar.command.bg = self._palette["background"]

        # Foreground color of the statusbar in command mode.
        c.colors.statusbar.command.fg = self._palette["pink"]

        # Background color of the statusbar in private browsing + command mode.
        c.colors.statusbar.command.private.bg = self._palette["background"]

        # Foreground color of the statusbar in private browsing + command mode.
        c.colors.statusbar.command.private.fg = self._palette["foreground-alt"]

        # Background color of the statusbar in insert mode.
        c.colors.statusbar.insert.bg = self._palette["background-attention"]

        # Foreground color of the statusbar in insert mode.
        c.colors.statusbar.insert.fg = self._palette["foreground-attention"]

        # Background color of the statusbar.
        c.colors.statusbar.normal.bg = self._palette["background"]

        # Foreground color of the statusbar.
        c.colors.statusbar.normal.fg = self._palette["foreground"]

        # Background color of the statusbar in passthrough mode.
        c.colors.statusbar.passthrough.bg = self._palette["background"]

        # Foreground color of the statusbar in passthrough mode.
        c.colors.statusbar.passthrough.fg = self._palette["orange"]

        # Background color of the statusbar in private browsing mode.
        c.colors.statusbar.private.bg = self._palette["background-alt"]

        # Foreground color of the statusbar in private browsing mode.
        c.colors.statusbar.private.fg = self._palette["foreground-alt"]

        # Background color of the progress bar.
        c.colors.statusbar.progress.bg = self._palette["background"]

        # Foreground color of the URL in the statusbar on error.
        c.colors.statusbar.url.error.fg = self._palette["red"]

        # Default foreground color of the URL in the statusbar.
        c.colors.statusbar.url.fg = self._palette["foreground"]

        # Foreground color of the URL in the statusbar for hovered links.
        c.colors.statusbar.url.hover.fg = self._palette["cyan"]

        # Foreground color of the URL in the statusbar on successful load
        c.colors.statusbar.url.success.http.fg = self._palette["green"]

        # Foreground color of the URL in the statusbar on successful load
        c.colors.statusbar.url.success.https.fg = self._palette["green"]

        # Foreground color of the URL in the statusbar when there's a warning.
        c.colors.statusbar.url.warn.fg = self._palette["yellow"]

        # Status bar padding
        c.statusbar.padding = self._padding

        # Background color of the tab bar.
        # Type: QtColor
        c.colors.tabs.bar.bg = self._palette["selection"]

        # Background color of unselected even tabs.
        # Type: QtColor
        c.colors.tabs.even.bg = self._palette["selection"]

        # Foreground color of unselected even tabs.
        # Type: QtColor
        c.colors.tabs.even.fg = self._palette["foreground"]

        # Color for the tab indicator on errors.
        # Type: QtColor
        c.colors.tabs.indicator.error = self._palette["red"]

        # Color gradient start for the tab indicator.
        # Type: QtColor
        c.colors.tabs.indicator.start = self._palette["orange"]

        # Color gradient end for the tab indicator.
        # Type: QtColor
        c.colors.tabs.indicator.stop = self._palette["green"]

        # Color gradient interpolation system for the tab indicator.
        # Type: ColorSystem
        # Valid values:
        #   - rgb: Interpolate in the RGB color system.
        #   - hsv: Interpolate in the HSV color system.
        #   - hsl: Interpolate in the HSL color system.
        #   - none: Don't show a gradient.
        c.colors.tabs.indicator.system = "none"

        # Background color of unselected odd tabs.
        # Type: QtColor
        c.colors.tabs.odd.bg = self._palette["selection"]

        # Foreground color of unselected odd tabs.
        # Type: QtColor
        c.colors.tabs.odd.fg = self._palette["foreground"]

        #  Background color of selected even tabs.
        #  Type: QtColor
        c.colors.tabs.selected.even.bg = self._palette["background"]

        #  Foreground color of selected even tabs.
        #  Type: QtColor
        c.colors.tabs.selected.even.fg = self._palette["foreground"]

        #  Background color of selected odd tabs.
        #  Type: QtColor
        c.colors.tabs.selected.odd.bg = self._palette["background"]

        #  Foreground color of selected odd tabs.
        #  Type: QtColor
        c.colors.tabs.selected.odd.fg = self._palette["foreground"]

        # Tab padding
        c.tabs.padding = self._padding
        c.tabs.indicator.width = 1
        c.tabs.favicons.scale = 1
