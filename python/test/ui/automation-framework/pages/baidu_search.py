#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import unittest
import sys
import os

sys.path.append(os.path.split(os.path.dirname(__file__))[0])
print(sys.path)
from commons.browser_engine import BrowserEngine
from commons.logger import Logger

log = Logger(logger='baidu_search').get_log()


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            log.info('Test pass.')
        except Exception as e:
            log.info('Test fail.')

if __name__ == '__main__':
    unittest.main()
