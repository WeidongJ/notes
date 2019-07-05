#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from framework.basepage import BasePage


class GamePage(BasePage):
    game_link = "xpath=>//div[@id='channel-all']/div/ul/li[10]"

    def click_sports(self):
        self.click(self.game_link)
        self.sleep(2)