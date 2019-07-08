#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import time
import os


class Logger(object):

    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq = time.strftime('%Y%m%d%H%M', time.localtime())
        log_path = os.path.dirname(__file__) + '/logs/'
        log_name = log_path + rq + '.log'

        # file handler  用于写入log文件
        fh = logging.FileHandler(log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # stream handler 用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        fh.close()
        ch.close()

    def get_log(self):
        return self.logger
