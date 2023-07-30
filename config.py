# REF:
#   qute://help/configuring.html
#   qute://help/settings.html


class Bind:
    @staticmethod
    def concat(commands: list[str]) -> str:
        return ";; ".join(commands)

    @staticmethod
    def repeat(command: str, repeat_for: int) -> list[str]:
        return repeat_for * [command]


class Configuration:
    def __init__(self, c, config):
        self._c, self._config = c, config

        self._misc()
        self._cookies()
        self._headers()
        self._ad_block()
        self._contents_to_load()
        self._edit()
        self._colorscheme()
        self._bind()

    def _misc(self) -> None:
        # only use self._config.py
        self._config.load_autoconfig(False)

        self._c.changelog_after_upgrade = "never"

        self._c.auto_save.session = True

    def _cookies(self) -> None:
        # Which cookies to accept. With QtWebEngine, this setting also controls
        # other features with tracking capabilities similar to those of cookies;
        # including IndexedDB, DOM storage, filesystem API, service workers, and
        # AppCache. Note that with QtWebKit, only `all` and `never` are
        # supported as per-domain values. Setting `no-3rdparty` or `no-
        # unknown-3rdparty` per-domain on QtWebKit will have the same effect as
        # `all`. If this setting is used with URL patterns, the pattern gets
        # applied to the origin/first party URL of the page making the request,
        # not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
        # from URLs, so URL patterns using paths will not match. With
        # QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
        # you will typically need to set this setting for `example.com` when the
        # cookie is set on `somesubdomain.example.com` for it to work properly.
        # To debug issues with this setting, start qutebrowser with `--debug
        # --logfilter network --debug-flag log-cookies` which will show all
        # cookies being set.
        # Type: String
        # Valid values:
        #   - all: Accept all cookies.
        #   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
        #   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
        #   - never: Don't accept cookies at all.
        self._config.set("content.cookies.accept", "all", "chrome-devtools://*")

        # Which cookies to accept. With QtWebEngine, this setting also controls
        # other features with tracking capabilities similar to those of cookies;
        # including IndexedDB, DOM storage, filesystem API, service workers, and
        # AppCache. Note that with QtWebKit, only `all` and `never` are
        # supported as per-domain values. Setting `no-3rdparty` or `no-
        # unknown-3rdparty` per-domain on QtWebKit will have the same effect as
        # `all`. If this setting is used with URL patterns, the pattern gets
        # applied to the origin/first party URL of the page making the request,
        # not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
        # from URLs, so URL patterns using paths will not match. With
        # QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
        # you will typically need to set this setting for `example.com` when the
        # cookie is set on `somesubdomain.example.com` for it to work properly.
        # To debug issues with this setting, start qutebrowser with `--debug
        # --logfilter network --debug-flag log-cookies` which will show all
        # cookies being set.
        # Type: String
        # Valid values:
        #   - all: Accept all cookies.
        #   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
        #   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
        #   - never: Don't accept cookies at all.
        self._config.set("content.cookies.accept", "all", "devtools://*")

    def _headers(self) -> None:
        # Value to send in the `Accept-Language` header. Note that the value
        # read from JavaScript is always the global value.
        # Type: String
        self._config.set(
            "content.headers.accept_language", "", "https://matchmaker.krunker.io/*"
        )

        # User agent to send.  The following placeholders are defined:  *
        # `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
        # The underlying WebKit version (set to a fixed value   with
        # QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
        # QtWebEngine. * `{qt_version}`: The underlying Qt version. *
        # `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
        # QtWebEngine. * `{upstream_browser_version}`: The corresponding
        # Safari/Chrome version. * `{qutebrowser_version}`: The currently
        # running qutebrowser version.  The default value is equal to the
        # unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
        # read from JavaScript is always the global value. With QtWebEngine
        # between 5.12 and 5.14 (inclusive), changing the value exposed to
        # JavaScript requires a restart.
        # Type: FormatString
        self._c.content.headers.user_agent = "/Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}"

        # User agent to send.  The following placeholders are defined:  *
        # `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
        # The underlying WebKit version (set to a fixed value   with
        # QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
        # QtWebEngine. * `{qt_version}`: The underlying Qt version. *
        # `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
        # QtWebEngine. * `{upstream_browser_version}`: The corresponding
        # Safari/Chrome version. * `{qutebrowser_version}`: The currently
        # running qutebrowser version.  The default value is equal to the
        # unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
        # read from JavaScript is always the global value. With QtWebEngine
        # between 5.12 and 5.14 (inclusive), changing the value exposed to
        # JavaScript requires a restart.
        # Type: FormatString
        self._config.set(
            "content.headers.user_agent",
            "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
            "https://web.whatsapp.com/",
        )

        # User agent to send.  The following placeholders are defined:  *
        # `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
        # The underlying WebKit version (set to a fixed value   with
        # QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
        # QtWebEngine. * `{qt_version}`: The underlying Qt version. *
        # `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
        # QtWebEngine. * `{upstream_browser_version}`: The corresponding
        # Safari/Chrome version. * `{qutebrowser_version}`: The currently
        # running qutebrowser version.  The default value is equal to the
        # unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
        # read from JavaScript is always the global value. With QtWebEngine
        # between 5.12 and 5.14 (inclusive), changing the value exposed to
        # JavaScript requires a restart.
        # Type: FormatString
        self._config.set(
            "content.headers.user_agent",
            "Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0",
            "https://accounts.google.com/*",
        )

        # User agent to send.  The following placeholders are defined:  *
        # `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
        # The underlying WebKit version (set to a fixed value   with
        # QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
        # QtWebEngine. * `{qt_version}`: The underlying Qt version. *
        # `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
        # QtWebEngine. * `{upstream_browser_version}`: The corresponding
        # Safari/Chrome version. * `{qutebrowser_version}`: The currently
        # running qutebrowser version.  The default value is equal to the
        # unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
        # read from JavaScript is always the global value. With QtWebEngine
        # between 5.12 and 5.14 (inclusive), changing the value exposed to
        # JavaScript requires a restart.
        # Type: FormatString
        self._config.set(
            "content.headers.user_agent",
            "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
            "https://*.slack.com/*",
        )

    def _ad_block(self) -> None:
        self._config.set("content.blocking.method", "both")

        adblock_lists = [
            (
                "https://pgl.yoyo.org/adservers/serverlist.php?"
                "hostformat=adblockplus&showintro=1&mimetype=plaintext"
            ),
            "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
            "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
            "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
            "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
            "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt",
            "https://easylist.to/easylist/easylist.txt",
            "https://easylist.to/easylist/easyprivacy.txt",
        ]
        self._config.set("content.blocking.adblock.lists", adblock_lists)

    def _contents_to_load(self) -> None:
        # Load images automatically in web pages.
        # Type: Bool
        self._config.set("content.images", True, "chrome-devtools://*")

        # Load images automatically in web pages.
        # Type: Bool
        self._config.set("content.images", True, "devtools://*")

        # Enable JavaScript.
        # Type: Bool
        self._config.set("content.javascript.enabled", True, "chrome-devtools://*")

        # Enable JavaScript.
        # Type: Bool
        self._config.set("content.javascript.enabled", True, "devtools://*")

        # Enable JavaScript.
        # Type: Bool
        self._config.set("content.javascript.enabled", True, "chrome://*/*")

        # Enable JavaScript.
        # Type: Bool
        self._config.set("content.javascript.enabled", True, "qute://*/*")

    def _edit(self) -> None:
        self._c.editor.command = [
            "foot",
            "nvim",
            "{file}",
            "-c",
            "normal {line}G{column0}l",
        ]

        self._c.spellcheck.languages = [
            "en-US",
            "fr-FR",
            "sv-SE",
            "de-DE",
            "it-IT",
            "es-ES",
            "pt-BR",
            "ru-RU",
        ]

    def _colorscheme(self) -> None:
        self._c.colors.webpage.preferred_color_scheme = "dark"

        self._c.colors.webpage.darkmode.enabled = False

    def _bind(self) -> None:
        self._c.bindings.key_mappings = {
            "<Ctrl+6>": "<Ctrl+^>",
            "<Ctrl+Enter>": "<Ctrl+Return>",
            "<Ctrl+i>": "<Tab>",
            "<Ctrl+j>": "<Return>",
            "<Ctrl+m>": "<Return>",
            "<Ctrl+[>": "<Escape>",
            "<Enter>": "<Return>",
            "<Shift+Enter>": "<Return>",
            "<Shift+Return>": "<Return>",
        }

        # Bindings for normal mode
        self._config.bind("M", "hint links spawn mpv {hint-url}")

        self._config.bind("<Ctrl+h>", "tab-prev")
        self._config.bind("<Ctrl+l>", "tab-next")
        self._config.bind("K", Bind.concat(Bind.repeat("scroll up", 4)))
        self._config.bind("J", Bind.concat(Bind.repeat("scroll down", 4)))


Configuration(c, config)
