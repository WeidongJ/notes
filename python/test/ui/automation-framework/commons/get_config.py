#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import os
from commons.logger import Logger

log = Logger(logger='config_read').get_log()


def get_config(section, key):
    try:
        config_file = os.path.split(os.path.dirname(__file__))[0] + '/config/config.ini'
        config = configparser.ConfigParser()
        config.read(config_file, encoding='utf-8')
        return config.get(section, key)
    except Exception as e:
        log.error('config read fail', format(e))
