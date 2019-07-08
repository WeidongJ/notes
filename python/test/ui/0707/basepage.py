#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import time
from testlogger import Logger

log = Logger(logger='basepage').get_log()


class BasePage(object):
    """selenium 页面常用操作"""

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def quit_browser(self):
        self.driver.quit()

    def get_screenshot(self):
        folder_path = os.path.dirname(__file__) + '/screenshots/'
        rq = time.strftime('%Y%m%d %H%M', time.localtime())
        screenshot_path = folder_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screenshot_path)
            log.info('截图已保存，文件名： %s' % screenshot_path)
        except Exception as e:
            log.error('截图异常', format(e))




















