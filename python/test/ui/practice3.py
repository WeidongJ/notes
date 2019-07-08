#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://mail.126.com/')
sleep(2)
driver.execute_script("window.alert('弹窗')")
driver.switch_to.alert.accept()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[@id='switchAccountLogin']").click()
driver.implicitly_wait(2)
loginFrame = driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")
driver.switch_to.frame(loginFrame)
sleep(0.5)
driver.find_element_by_xpath("//input[@name='email']").send_keys('123')
driver.find_element_by_xpath("//input[@name='password']").send_keys('123')
driver.find_element_by_xpath("//div[@class='f-cb loginbox']/a[@id='dologin']").click()
driver.get_screenshot_as_file('screenshot.png')



