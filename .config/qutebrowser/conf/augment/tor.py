from ..util.cmd import Cmd


class Tor:
    def __init__(self):
        (
            self._config_engines,
            self._engines_activated,
            self._engines_deactivated,
        ) = self._make_engines()

        self._config_proxy = "content.proxy"
        self._proxy_activated, self._proxy_deactivated = (
            "socks://localhost:9050/",
            "system",
        )

    def _make_engines(self) -> tuple[str, dict, dict]:
        engines_nontor = {
            "duck": self._make_duck_search_string("https://duckduckgo.com/"),
            "brave": self._make_brave_search_string("https://search.brave.com/"),
        }
        engines_tor = {
            "duck": self._make_duck_search_string(
                "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/"
            ),
            "brave": self._make_brave_search_string(
                "https://search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/"
            ),
        }

        return (
            "url.searchengines",
            {
                "DEFAULT": engines_tor["duck"],
                "d": engines_tor["duck"],
                "dn": engines_nontor["duck"],
                "b": engines_tor["brave"],
                "bn": engines_nontor["brave"],
            },
            {
                "DEFAULT": engines_nontor["duck"],
                "d": engines_nontor["duck"],
                "b": engines_nontor["brave"],
            },
        )

    @staticmethod
    def _make_duck_search_string(url) -> str:
        return url + "?q={}"

    @staticmethod
    def _make_brave_search_string(url) -> str:
        return url + "search?q={}"

    def activate(self, config) -> None:
        config.set(self._config_proxy, self._proxy_activated)

        self._set_engines(config, self._engines_activated)

    def deactivate(self, config) -> None:
        config.set(self._config_proxy, self._proxy_deactivated)

        self._set_engines(config, self._engines_deactivated)

    def _set_engines(self, config, engines: dict) -> None:
        config.set(self._config_engines, engines)

    def as_cmd(self, activate: bool) -> str:
        if activate:
            proxy = self._proxy_activated
            engines = self._engines_activated
        else:
            proxy = self._proxy_deactivated
            engines = self._engines_deactivated

        return Cmd.set_config_items(
            zip([self._config_proxy, self._config_engines], [proxy, engines])
        )
