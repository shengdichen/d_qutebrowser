from conf import visual, bind, webcontent, general, alias

# REF:
#   qute://help/configuring.html
#   qute://help/settings.html


class Configuration:
    def __init__(self, config):
        self._config = config

        alias.Alias(self._config).apply()
        general.MiscConf(self._config)
        webcontent.WebContent(self._config)
        visual.Visual(self._config).apply()
        bind.Bind(self._config).apply()


Configuration(config)
