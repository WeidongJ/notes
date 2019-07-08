#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os
import re
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

# dripath = os.path.dirname(__file__)

# driver = webdriver.Ie(dripath + '/api-auto-test/tools/IEDriverServer.exe')
driver.get('https://www.baidu.com')
driver.set_window_size(1280, 800)  # 设置窗口大小
time.sleep(2)
print(driver.capabilities['browserName'])
print(driver.capabilities['browserVersion'])  # 打印浏览器版本
print(driver.current_url)  # 获取url
print(driver.title)  # 获取title
assert u'百度一下' in driver.title
print(driver.find_element_by_xpath("//input[@id='kw']").size)  # 获取元素大小
# driver.maximize_window()
el = driver.find_element_by_tag_name('body')
el.click()  # selenium 3需要click
el.send_keys(Keys.CONTROL + 'a')
el2 = driver.find_element_by_tag_name('body')
el2.click()
el2.send_keys(Keys.CONTROL + 't')
time.sleep(5)
print(1)
print(driver.find_element_by_xpath("//p[@id='lh']//a[2]").text)  # 打印文本
driver.find_element_by_xpath("//p[@id='lh']//a[2]").click()
print
driver.back()
time.sleep(3)
driver.forward()
time.sleep(5)
'''
driver.get('https://news.baidu.com')
try:
        driver.find_element_by_xpath("//*[id='news']").is_selected()
        print('Test success')
except Exception as e:
        print('Test fail', format(e))

open_js = 'window.open("http://www.sougou.com")'
driver.execute_script(open_js)
'''
driver.find_element_by_xpath("//ul[@class='bd-nav']//a[contains(text(),'联系我们')]").click()
time.sleep(5)
c_hander = driver.current_window_handle
for hander in driver.window_handles:
    if hander != c_hander:
        driver.close()
        print(hander)
        driver.switch_to.window(hander)

doc = driver.page_source  # 获取页面源码
emails = re.findall(r'\w+@[\w\.-]+', doc)
for email in emails:
    print(email)
# driver.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')
# driver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(8)
driver.close()
