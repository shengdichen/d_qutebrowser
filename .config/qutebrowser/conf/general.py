class MiscConf:
    def __init__(self, config):
        self._config = config

        self._misc()
        self._hint()
        self._default_pages()
        self._tabs()
        self._edit()

    def _misc(self) -> None:
        # only use self._config.py
        self._config.load_autoconfig(False)

        self._config.set("changelog_after_upgrade", "never")

    def _hint(self) -> None:
        base = "hints."

        self._config.set(f"{base}uppercase", True)
        self._config.set(f"{base}mode", "letter")
        # use easily distinguishable majuscules
        self._config.set(f"{base}chars", "azwsxeholp")

    def _default_pages(self) -> None:
        self._config.set("auto_save.session", False)
        self._config.set("session.default_name", "def")
        self._config.set("session.lazy_restore", True)

        self._config.set("url.start_pages", "https://shengdichen.xyz")  # on launch
        self._config.set("url.default_page", "about:blank")  # when opening new tab

    def _tabs(self) -> None:
        base = "tabs."
        self._config.set(f"{base}last_close", "close")
        self._config.set(f"{base}mousewheel_switching", False)
        for item in ["related", "unrelated"]:
            self._config.set(f"{base}new_position.{item}", "next")

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
