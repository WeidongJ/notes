#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import unittest
import sys
import os
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from commons.browser_engine import BrowserEngine
from pages.baidu_homepage import HomePage
from commons.logger import Logger

log = Logger(logger='baidusearch').get_log()


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.submit_btn()
        time.sleep(2)
        homepage.get_screenshot()
        assert 'selenium' in homepage.get_page_title()
        log.info('test pass.')

if __name__ == "__main__":
    unittest.main()

