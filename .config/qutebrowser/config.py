from conf import visual, bind, webcontent, general, alias
from conf.augment import tor

# REF:
#   qute://help/configuring.html
#   qute://help/settings.html


class Configuration:
    def __init__(self, config):
        self._config = config

        general.MiscConf(self._config)
        webcontent.WebContent(self._config)
        visual.Visual(self._config).apply()
        bind.Bind(self._config)

        self._alias = alias.Alias(self._config)

        self._augment()
        self._finalize()

    def _augment(self) -> None:
        self._tor()

    def _tor(self) -> None:
        conf = tor.Tor()
        conf.deactivate(self._config)

        self._alias.add("tor_on", conf.as_cmd(activate=True))
        self._alias.add("tor_off", conf.as_cmd(activate=False))

    def _finalize(self) -> None:
        self._alias.apply()


Configuration(config)
