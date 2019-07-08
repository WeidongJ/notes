#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 模拟键盘的方法
from selenium.webdriver.common.action_chains import ActionChains  # 模拟键盘操作
from time import sleep
import os
import win32api
import win32con

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')
sleep(2)

driver.find_element_by_xpath("//input[@id='kw']").clear()
# driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.CONTROL + 'a')
# driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.BACKSPACE)
sleep(2)
driver.get('https://www.baidu.com')
sleep(2)
el = driver.find_element_by_xpath("//div[@id='lg']/img")
right_click = ActionChains(driver)
right_click.context_click(el).perform()
sleep(2)

# 定义好键盘对应的编码
VK_Code = {'enter': 0x0D, 'down_arrow': 0x28, 'k': 0x4B, 'v': 0x56}


# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_Code[keyName], 0, 0, 0)


# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_Code[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


keyDown('k')
keyUp('k')
sleep(2)
keyDown('enter')
keyUp('enter')
sleep(2)
driver.close()
