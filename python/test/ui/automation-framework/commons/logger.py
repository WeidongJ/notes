#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import time


class Logger(object):

    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # file handler 处理log文件
        log_dir = os.path.split(os.path.dirname(__file__))[0] + '/logs/'
        ct = time.strftime('%Y%m%d%H%M', time.localtime())
        log_file = log_dir + ct + '.log'
        fh = logging.FileHandler(log_file, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # stream handler 终端输出
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        fh.close()
        ch.close()

    def get_log(self):
        return self.logger
