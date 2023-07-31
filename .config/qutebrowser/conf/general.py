class _TorConf:
    def __init__(self):
        self._engines_nontor = {
            "duck": self._make_duck_search_string("https://duckduckgo.com/"),
            "brave": self._make_brave_search_string("https://search.brave.com/"),
        }

        self._engines_tor = {
            "duck": self._make_duck_search_string(
                "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/"
            ),
            "brave": self._make_brave_search_string(
                "https://search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/"
            ),
        }

    @staticmethod
    def _make_duck_search_string(url) -> str:
        return url + "?q={}"

    @staticmethod
    def _make_brave_search_string(url) -> str:
        return url + "search?q={}"

    def activate(self, config) -> None:
        config.set("content.proxy", "socks://localhost:9050/")

        self._set_engines(
            config,
            {
                "DEFAULT": self._engines_tor["duck"],
                "d": self._engines_tor["duck"],
                "dn": self._engines_nontor["duck"],
                "b": self._engines_tor["brave"],
                "bn": self._engines_nontor["brave"],
            },
        )

    def deactivate(self, config) -> None:
        config.set("content.proxy", "")

        self._set_engines(
            config,
            {
                "DEFAULT": self._engines_nontor["duck"],
                "d": self._engines_nontor["duck"],
                "b": self._engines_nontor["brave"],
            },
        )

    @staticmethod
    def _set_engines(config, engines: dict) -> None:
        config.set("url.searchengines", engines)


class MiscConf:
    def __init__(self, config):
        self._config = config

        self._misc()
        _TorConf().activate(self._config)
        self._default_pages()
        self._edit()

    def _misc(self) -> None:
        # only use self._config.py
        self._config.load_autoconfig(False)

        self._config.set("changelog_after_upgrade", "never")

    def _default_pages(self) -> None:
        self._config.set("auto_save.session", False)
        self._config.set("session.default_name", "def")
        self._config.set("session.lazy_restore", True)

        self._config.set("url.start_pages", "https://shengdichen.xyz")  # on launch
        self._config.set("url.default_page", "about:blank")  # when opening new tab

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
