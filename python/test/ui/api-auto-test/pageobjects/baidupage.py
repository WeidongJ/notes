#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from framework.basepage import BasePage


class BaiduPage(BasePage):

    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    news_link = "xpath=>//a[@name='tj_trnews']"

    def type_search(self,text):
        self.typing(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.sleep(5)

    