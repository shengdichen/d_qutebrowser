class Tor:
    def __init__(self):
        self._config_engines = "url.searchengines"
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

        self._engines_activated = {
            "DEFAULT": self._engines_tor["duck"],
            "d": self._engines_tor["duck"],
            "dn": self._engines_nontor["duck"],
            "b": self._engines_tor["brave"],
            "bn": self._engines_nontor["brave"],
        }
        self._engines_deactivated = {
            "DEFAULT": self._engines_nontor["duck"],
            "d": self._engines_nontor["duck"],
            "b": self._engines_nontor["brave"],
        }

        self._config_proxy = "content.proxy"
        self._proxy_activated, self._proxy_deactivated = (
            "socks://localhost:9050/",
            "system",
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

        cmd_proxy = " ".join(["set", self._config_proxy, proxy])
        cmd_engines = " ".join(["set", self._config_engines, f'"{engines}"'])

        return ";; ".join([cmd_proxy, cmd_engines])
