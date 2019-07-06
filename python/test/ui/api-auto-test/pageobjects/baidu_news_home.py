#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from framework.basepage import BasePage


class NewsPage(BasePage):
    sports_link = "xpath=>//div[@id='channel-all']/div/ul/li[7]"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)