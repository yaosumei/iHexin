#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_object.appium_page_objects import PageObject, page_element
class ZixuangufenzuPage(PageObject):
    xinjianfenzu_btn = page_element(accessibility_id = "新建分组")
    guanlifenzu_btn = page_element(accessibility_id = "管理分组")
    zixuangu_btn = page_element(accessibility_id="自选股")
    bankuai1_btn = page_element(accessibility_id="板块1")
    bankuai2_btn = page_element(accessibility_id="板块2")
    bankuai3_btn = page_element(accessibility_id="板块3")
    bankuai4_btn = page_element(accessibility_id="板块4")
    bankuai5_btn = page_element(accessibility_id="板块5")
    bankuai6_btn = page_element(accessibility_id="板块6")
    bankuai7_btn = page_element(accessibility_id="板块7")
    bankuai8_btn = page_element(accessibility_id="板块8")

    chakanxiangqing_btn = page_element(accessibility_id = "查看详情")
    guanbi_btn = page_element(accessibility_id = "关闭")