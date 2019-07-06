#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidupage import BaiduPage
from pageobjects.baidu_news_home import NewsPage
from pageobjects.baidu_game_home import GamePage


class BaiduSearch1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search1(self):
        homepage = BaiduPage(self.driver)
        homepage.click_news()
        newshome = NewsPage(self.driver)
        newshome.click_sports()
        sportshome = GamePage(self.driver)
        sportshome.click_sports()
        time.sleep(2)
<<<<<<< HEAD
        homepage.take_screenshot()

        
'''
=======
        homepage.take_screen_shot()
    """
>>>>>>> c2ef97a236eded824586a7c300dc1f1529defbe6
    def test_search2(self):
        homepage = BaiduPage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.take_screen_shot()
        """


if __name__ == '__main__':
    unittest.main()