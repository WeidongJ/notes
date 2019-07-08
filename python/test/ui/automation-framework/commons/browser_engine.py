#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import configparser
import os
from selenium import webdriver
from commons.logger import Logger
from commons.get_config import get_config

log = Logger(logger='browser_engine').get_log()


class BrowserEngine(object):

    # 浏览器驱动文件
    tool_dir = os.path.split(os.path.dirname(__file__))[0] + '/tools/'
    chrome_driver = tool_dir + 'chromedriver.exe'
    ie_driver = tool_dir + 'IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        browser = get_config('browser', 'browser')
        log.info('browser_type: %s' % browser)
        url = get_config('test_server', 'url')
        log.info('Test server: %s' % url)

        if 'ie' in browser.lower():
            self.driver = webdriver.Ie(self.ie_driver)
            log.info('Starting ie browser')
        elif 'firefox' in browser.lower():
            self.driver = webdriver.Firefox()
            log.info('Starting firefox browser')
        else:
            self.driver = webdriver.Chrome(self.chrome_driver)
            log.info('Starting chrome browser')

        # open url
        self.driver.get(url)
        log.info('Open url is: %s' % url)   
        self.driver.implicitly_wait(5)
        log.info('Set implicitly wait 5 seconds.')
        return self.driver

    def quit_browser(self):
        self.driver.quit()
        log.info('quit browser.')
