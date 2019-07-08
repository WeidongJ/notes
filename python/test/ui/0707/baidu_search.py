#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from basepage import BasePage


class BaiduSearch(object):

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    basepage = BasePage(driver)

    def open_baidu(self, url):
        self.basepage.open_url(url)
        sleep(1)

    def search(self, key_word):
        self.driver.find_element_by_id('kw').send_keys(key_word)
        self.basepage.get_screenshot()
        sleep(1)
        self.basepage.back()
        self.basepage.forward()
        self.basepage.quit_browser()

baidu = BaiduSearch()
baidu.open_baidu('https://www.baidu.com')
baidu.search('selenium')
