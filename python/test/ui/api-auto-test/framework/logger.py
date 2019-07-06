#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# logging

import logging
import time
import os


class Logger(object):

    def __init__(self, logger):
        """指定保存日志路径，日志级别，以及调用文件
        将日志存入到指定的文件中去
        """
        # 创建一个Logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志
        current_time = time.strftime('%Y%m%d%H%M', time.localtime())
        log_path = os.path.split(os.path.dirname(__file__))[0] + '/logs/'
        log_name = log_path + current_time + '.log'
        fh = logging.FileHandler(log_name, encoding='utf-8')  # 指定file handler编码
        fh.setLevel(logging.INFO)

        # 输出handler 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler输出格式

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
