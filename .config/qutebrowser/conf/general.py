class MiscConf:
    def __init__(self, config):
        self._config = config

        self._misc()
        self._default_pages()
        self._search()
        self._edit()

    def _misc(self) -> None:
        # only use self._config.py
        self._config.load_autoconfig(False)

        self._config.set("changelog_after_upgrade", "never")

    def _default_pages(self) -> None:
        self._config.set("session.default_name", "def")
        self._config.set("auto_save.session", True)

        self._config.set("url.start_pages", "https://shengdichen.xyz")  # on launch
        self._config.set("url.default_page", "about:blank")  # when opening new tab

    def _search(self) -> None:
        duck = "https://duckduckgo.com/?q={}"
        brave = "https://search.brave.com/search?q={}"

        self._config.set(
            "url.searchengines",
            {"DEFAULT": duck, "d": duck, "b": brave},
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
