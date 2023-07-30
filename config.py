from conf import visual, bind, webcontent

# REF:
#   qute://help/configuring.html
#   qute://help/settings.html


class Configuration:
    def __init__(self, config):
        self._config = config

        self._misc()
        webcontent.WebContent(self._config)
        self._edit()
        self._visual()
        self._bind()

    def _misc(self) -> None:
        # only use self._config.py
        self._config.load_autoconfig(False)

        self._config.set("changelog_after_upgrade", "never")

        self._config.set("auto_save.session", True)

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

    def _visual(self) -> None:
        v = visual.Visual(self._config)
        v.apply()

    def _bind(self) -> None:
        b = bind.Bind(self._config)
        b.apply()


Configuration(config)
