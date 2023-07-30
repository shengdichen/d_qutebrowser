class MiscConf:
    def __init__(self, config):
        self._config = config

        self._misc()
        self._use_tor()
        self._default_pages()
        self._search()
        self._edit()

    def _misc(self) -> None:
        # only use self._config.py
        self._config.load_autoconfig(False)

        self._config.set("changelog_after_upgrade", "never")

    def _use_tor(self) -> None:
        self._config.set("content.proxy", "socks://localhost:9050/")

    def _default_pages(self) -> None:
        self._config.set("auto_save.session", False)
        self._config.set("session.default_name", "def")
        self._config.set("session.lazy_restore", True)

        self._config.set("url.start_pages", "https://shengdichen.xyz")  # on launch
        self._config.set("url.default_page", "about:blank")  # when opening new tab

    def _search(self) -> None:
        duck = "https://duckduckgo.com/?q={}"
        duck_tor = "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/?q={}"
        brave = "https://search.brave.com/search?q={}"
        brave_tor = "https://search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/search?q={}"

        self._config.set(
            "url.searchengines",
            {"DEFAULT": duck, "d": duck, "dt": duck_tor, "b": brave, "bt": brave_tor},
        )

    def _edit(self) -> None:
        self._config.set(
            "editor.command",
            [
                "foot",
                "nvim",
                "{file}",
                "-c",
                "normal {line}G{column0}l",
            ],
        )

        self._config.set(
            "spellcheck.languages",
            [
                "en-US",
                "fr-FR",
                "sv-SE",
                "de-DE",
                "it-IT",
                "es-ES",
                "pt-BR",
                "ru-RU",
            ],
        )
