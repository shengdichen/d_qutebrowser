class WebContent:
    def __init__(self, config):
        self._config = config

        self._cookies()
        self._headers()
        self._ad_block()
        self._contents_to_load()

    def _cookies(self) -> None:
        # accept cookies by default
        self._config.set("content.cookies.accept", "all")

        self._config.set("content.cookies.accept", "all", "devtools://*")
        self._config.set("content.cookies.accept", "all", "chrome-devtools://*")

    def _headers(self) -> None:
        self._config.set(
            "content.headers.accept_language", "", "https://matchmaker.krunker.io/*"
        )

        self._config.set(
            "content.headers.user_agent",
            (
                "/Mozilla/5.0 ({os_info}) "
                "AppleWebKit/{webkit_version} (KHTML, like Gecko) "
                "{qt_key}/{qt_version} "
                "{upstream_browser_key}/{upstream_browser_version} "
                "Safari/{webkit_version}"
            ),
        )
        self._config.set(
            "content.headers.user_agent",
            (
                "Mozilla/5.0 ({os_info}) "
                "AppleWebKit/{webkit_version} (KHTML, like Gecko) "
                "{upstream_browser_key}/{upstream_browser_version} "
                "Safari/{webkit_version}"
            ),
            "https://web.whatsapp.com/",
        )
        self._config.set(
            "content.headers.user_agent",
            "Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0",
            "https://accounts.google.com/*",
        )
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
