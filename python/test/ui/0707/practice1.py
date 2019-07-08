#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver


class BaiduSearch(object):

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    def open_baidu(self):
        self.driver.get('https://www.baidu.com')
        sleep(1)

    def search(self, key_word):
        self.driver.find_element_by_xpath("//input[@id='kw']").send_keys(key_word)
        sleep(1)
        print(self.driver.title)
        try:
            assert key_word in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def quit(self):
        self.driver.quit()
baidu = BaiduSearch()
baidu.open_baidu()
baidu.search('selenium')
baidu.quit()
