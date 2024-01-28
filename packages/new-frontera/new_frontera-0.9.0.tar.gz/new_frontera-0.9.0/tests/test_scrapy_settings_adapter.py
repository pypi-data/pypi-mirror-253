# -*- coding: utf-8 -*-

from __future__ import absolute_import
from new_frontera.contrib.scrapy.settings_adapter import ScrapySettingsAdapter


def test_fallsback_to_crawler_settings():
    settings = ScrapySettingsAdapter({"DELAY_ON_EMPTY": 10})
    assert settings.get("DELAY_ON_EMPTY") == 10


def test_new_frontera_settings_have_precedence_over_crawler_settings():
    crawler_settings = {
        "MAX_REQUESTS": 10,
        "new_frontera_SETTINGS": "tests.scrapy_spider.new_frontera.settings",
    }
    settings = ScrapySettingsAdapter(crawler_settings)
    assert settings.get("MAX_REQUESTS") == 5
