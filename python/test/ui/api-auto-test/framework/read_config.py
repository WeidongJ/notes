#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import configparser


class ConfigRead(object):
	
    config = configparser.ConfigParser()

    def get_value(self, section, key):
        root_path = os.path.split(os.path.dirname(__file__))[0]
        file_path = root_path + '/config/config.ini'
        try:
            config.read(file_path)
            return config.get(section, key)
        except Exception as e:
            print('config read fail.', format(e))


config = ConfigRead()
print(config.get_value('host', 'url'))