#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException

'''base operation'''

my_logger = Logger(logger='BasePage').get_log()



class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def open_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def take_screen_shot(self):
        img_path = os.path.split(os.path.dirname(__file__))[0] + '/screenshots/'
        current_time = time.strftime('%Y%m%d%H%M', time.localtime())
        screen_name = img_path + current_time + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            my_logger.info('开始截图并保存')
        except Exception as e:
            print('截图失败', format(e))

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                my_logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                my_logger.error("NoSuchElementException: %s" % e)
                self.take_screen_shot()   # take screen_shot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(
                selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                my_logger.info("Had find the element \' %s \' successful "
                                "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                my_logger.error("NoSuchElementException: %s" % e)
                self.take_screen_shot()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def typing(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            my_logger.info('输入文本：%s' % text)
        except NameError as e:
            my_logger.error('Failed to type in input box with :%s' % e)
            self.take_screen_shot()

    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            my_logger.info('clear text box.')
        except NameError as e:
            my_logger.error('Failed to clear text box with:%s' % e)
            self.take_screen_shot()

    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            my_logger.info('element click success.')
        except NameError as e:
            my_logger.error('Failed to clear text box with:%s' % e)
            self.take_screen_shot()
        
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        my_logger.info('Sleep for %s seconds.' % seconds)
