#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os

# driver = webdriver.Firefox()
# driver = webdriver.Chrome()

dripath = os.path.dirname(__file__)

driver = webdriver.Ie(dripath + '/api-auto-test/tools/IEDriverServer.exe')
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(4)
time.sleep(2)
driver.close()