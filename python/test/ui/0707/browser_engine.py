#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver


class BrowserEngine(object):

    def __init__(self, driver, browser):
        self.driver = driver
        self.browser = browser

    def get_browser(self):
        if 'ie' in self.browser.lower():
            self.driver = webdriver.Ie()
        elif 'firefox' in self.browser.lower():
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(8)
        return self.driver


class TestBrowserEngine(object):

    def open_browser(self):
        browser = BrowserEngine(self, 'chrome')
        driver = browser.get_browser()

tbe = TestBrowserEngine()
tbe.open_browser()