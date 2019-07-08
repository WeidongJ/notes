#!/usr/bin/env python3
# -*- codin: utf-8 -*- 

import unittest
import time
from selenium import webdriver
from testlogger import Logger

log = Logger(logger='unittest').get_log()



class BaiduSearch(unittest.TestCase):

    def setUp(self):
        '''
        用例执行前的初始化工作。
        '''
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        '''
        用例执行结束后的清理工作
        '''
        self.driver.quit()

    def test_search(self):
        '''
        test case
        '''
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
        except Exception as e:
            log.error('assert fail', format(e))

if __name__ == '__main__':
    unittest.main()

