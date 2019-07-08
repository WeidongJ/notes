#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium.common.exceptions import NoSuchElementException
import os
from commons.logger import Logger

log = Logger(logger='basepage').get_log()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def wait(self, seconds):
        self.driver.implicity_wait(seconds)
        log.info('implicity wait %s s' % seconds)

    def close(self):
        try:
            self.driver.close()
        except NameError as e:
            log.error('Failed to close browser with %s' % e)

    def get_screenshot(self):
        dir_screenshot = os.path.split(os.path.dirname(__file__))[0] + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime())
        screenshot_file = dir_screenshot + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screenshot_file)
            log.info('get screenshot %s success.' % screenshot_file)
        except NameError as e:
            log.error('fail to get screenshots with %s' % e)
            self.get_screenshot()

    def find_element(self, selector):
        '''
        封装查找元素的方法
        '''
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by, selector_value = selector.split('=>')
        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                log.info('find element by id: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'n' or selector_by == 'name':
            try:
                element = self.driver.find_element_by_name(selector_value)
                log.info('find element by name: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'c' or selector_by == 'class_name':
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                log.info('find element by class_name: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'l' or selector_by == 'link_text':
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                log.info('find element by link_text: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                log.info('find element by partial_link_text: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 't' or selector_by == 'tag_name':
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                log.info('find element by tag_name: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                log.info('find element by xpath: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 's' or selector_by == 'css_selector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                log.info('find element by css_selector: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        else:
            raise NameError('target elements is invalid.')

        return element

    # 获取多个元素
    def find_elements(self, selector):   
        '''
        封装查找元素的方法
        '''
        elements = []
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by, selector_value = selector.split('=>')
        if selector_by == 'i' or selector_by == 'id':
            try:
                elements = self.driver.find_elements_by_id(selector_value)
                log.info('find elements by id: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Elements: %s' % e)
                self.get_screenshot()
        elif selector_by == 'n' or selector_by == 'name':
            try:
                elements = self.driver.find_elements_by_name(selector_value)
                log.info('find elements by name: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'c' or selector_by == 'class_name':
            try:
                elements = self.driver.find_elements_by_class_name(selector_value)
                log.info('find elements by class_name: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'l' or selector_by == 'link_text':
            try:
                elements = self.driver.find_elements_by_link_text(selector_value)
                log.info('find elements by link_text: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            try:
                elements = self.driver.find_elements_by_partial_link_text(selector_value)
                log.info('find elements by partial_link_text: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 't' or selector_by == 'tag_name':
            try:
                elements = self.driver.find_elements_by_tag_name(selector_value)
                log.info('find elements by tag_name: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
                log.info('find elements by xpath: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        elif selector_by == 's' or selector_by == 'css_selector':
            try:
                elements = self.driver.find_elements_by_css_selector(selector_value)
                log.info('find elements by css_selector: %s' % selector_value)
            except NoSuchElementException as e:
                log.error('No Such Element: %s' % e)
                self.get_screenshot()
        else:
            raise NameError('target elements is invalid.')

        return elements

    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            log.info('input text: %s success.' % text)
        except NameError as e:
            log.error('input textfailed with: %s' % e)
            self.get_screenshot()

    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            log.info('clear input box success.')
        except NameError as e:
            log.error('clear input box failed with: %s' % e)
            self.get_screenshot()

    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            log.info('click element: %s success.' % selector)
        except NameError as e:
            log.error('click element failed with:%s' % e)
            self.get_screenshot()
        
    def get_page_title(self):
        log.info('get page title success.')
        return self.driver.title
    
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        log.info('sleep %s s' % seconds)
 

            