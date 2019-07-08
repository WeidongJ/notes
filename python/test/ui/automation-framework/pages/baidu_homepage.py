#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from commons.base_page import BasePage


class HomePage(BasePage):
    input_box = 'id=>kw'
    search_btn = "xpath=>//input[@id='su']"

    def type_search(self, text):
        self.type(self.input_box, text)

    def submit_btn(self):
        self.click(self.search_btn)