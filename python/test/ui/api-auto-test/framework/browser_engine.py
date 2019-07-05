#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from framework.read_config import ConfigRead
from framework.logger import Logger
from selenium import webdriver
import os

logger = Logger(logger='BrowserEngine').get_log()

class BrowserEngine(object):

    dri_path = os.path.split(os.path.dirname(__file__))[0]
    chrome_dri_path = dri_path + '/tools/chromedriver.exe'
    ie_dri_path = dri_path + '/tools/IEDriverServer.exe'
    fireFox_dri_path = dri_path + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = ConfigRead()
        url = config.get_value('host','url')
        logger.info('Test url is: %s' % url)
        browser = config.get_value('browserType', 'browserName')
        logger.info('Test browser is: %s' % browser)

        if browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_dri_path)
            logger.info('Start Chrome browser.')
        elif browser == 'Firefox':
            driver = webdriver.Firefox(self.fireFox_dri_path)
            logger.info('Start Firefox browser.')
        elif browser == 'IE':
            driver = webdriver.Firefox(self.ie_dri_path)
            logger.info('Start Internet Explore.')

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def quit_browser(self):
        logger.info('Now quit browser.')
        self.driver.quit()