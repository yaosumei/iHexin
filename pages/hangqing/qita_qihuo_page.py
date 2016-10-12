#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tianmaotao"

from page_object.appium_page_objects import PageObject, page_element

class QitaQihuoPage(PageObject):
    fanhui_button = page_element(accessibility_id='返回')

    zhangfu_statictext = page_element(accessibility_id = '涨幅')
    zhangdie_statictext = page_element(accessibility_id='涨跌')

