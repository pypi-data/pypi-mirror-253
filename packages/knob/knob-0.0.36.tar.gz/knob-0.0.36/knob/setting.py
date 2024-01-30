# -*- coding:utf-8 -*-

import os
import six
from django.conf import settings

__all__ = ['get_setting', 'set_setting', 'turn_on_debug', 'turn_off_debug', 'is_debug_on']

setting_pool = []
dynamic_setting = None
constance_config = None

_INITED = False

_DEBUG = 'DEBUG_KNOB_SETTING' in os.environ
_DEBUG_SETTINGS_DICT = {}


def turn_on_debug():
    global _DEBUG
    _DEBUG = True


def turn_off_debug():
    global _DEBUG
    _DEBUG = False
    _DEBUG_SETTINGS_DICT.clear()


def is_debug_on():
    return _DEBUG


def get_setting(key, default=None):
    global _INITED
    if not _INITED:
        _init_knob_setting()

    global setting_pool

    if is_debug_on() and key in _DEBUG_SETTINGS_DICT:
        return _DEBUG_SETTINGS_DICT[key]

    res = default
    for setting in setting_pool:
        if hasattr(setting, key):
            res = getattr(setting, key)
    return res


def set_setting(key, value):
    global _INITED
    if not _INITED:
        _init_knob_setting()

    global constance_config

    if is_debug_on():
        _DEBUG_SETTINGS_DICT[key] = value
    else:
        if dynamic_setting == 'Constance':
            setattr(constance_config, key, value)
        else:
            raise RuntimeError("No dynamic setting module installed.")


def _init_knob_setting():
    global dynamic_setting
    global constance_config
    global _INITED

    if 'constance' in settings.INSTALLED_APPS:
        try:
            from constance import config as constance_config_
            constance_config = constance_config_
            setting_pool.append(constance_config)
            dynamic_setting = 'Constance'
        except ImportError:
            constance_config = None

    setting_pool.append(settings)

    _INITED = True
