from conf import visual, bind, webcontent, general

# REF:
#   qute://help/configuring.html
#   qute://help/settings.html


class Configuration:
    def __init__(self, config):
        self._config = config

        general.MiscConf(self._config)
        webcontent.WebContent(self._config)
        self._visual()
        self._bind()

    def _visual(self) -> None:
        v = visual.Visual(self._config)
        v.apply()

    def _bind(self) -> None:
        b = bind.Bind(self._config)
        b.apply()


Configuration(config)
