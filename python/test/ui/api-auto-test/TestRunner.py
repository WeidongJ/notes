#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
import os
import HTMLTestRunner
import time
from framework.sendMail import send_mail

from testsuits.test_baidu1 import BaiduSearch1
from testsuits.test_baidu import BaiduSearch

report_path = os.path.dirname(__file__) + '/reports/'

now = time.strftime('%Y%m%d%H%M', time.localtime())

report_html = report_path + now + 'HTMLreport.html'
fp = open(report_html, 'wb')

# 加载目录下的测试套
suite = unittest.TestLoader().discover('testsuits')
# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch1)) # 加载测试套
# suite.addTest(BaiduSearch('test_search'))
if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'项目测试报告', description=u'xxx项目测试报告')
    runner.run(suite)
    fp.close()
    send_mail(report_html)


