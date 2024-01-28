from __future__ import absolute_import
from new_frontera.settings import BaseSettings, DefaultSettings


class ScrapySettingsAdapter(BaseSettings):
    """
    Wrapps the new_frontera settings, falling back to scrapy and default settings
    """

    def __init__(self, crawler_settings):
        new_frontera_settings = crawler_settings.get("new_frontera_SETTINGS", None)
        super(ScrapySettingsAdapter, self).__init__(module=new_frontera_settings)
        self._crawler_settings = crawler_settings or {}
        self._default_settings = DefaultSettings()

    def get(self, key, default_value=None):
        val = super(ScrapySettingsAdapter, self).get(key)
        if val is not None:
            return val

        val = self._crawler_settings.get(key)
        if val is not None:
            return val

        return self._default_settings.get(key, default_value)
