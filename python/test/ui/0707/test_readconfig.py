#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import configparser
import os


def get_config(section, key):
    try:
        config_file = os.path.dirname(__file__) + '/config/config.ini'
        config = configparser.ConfigParser()
        config.read(config_file)
        return config.get(section, key)
    except Exception as e:
        print('Read config failed.', format(e))
