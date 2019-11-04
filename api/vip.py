#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     vip
   Description :
   Author :        Meiyo
   date：          2019/10/23 15:25
-------------------------------------------------
   Change Activity:
                   2019/10/23:
------------------------------------------------- 
"""
__author__ = 'Meiyo'
from airtest.core.api import touch, Template


# 会员手机号18621902561
def search_vip(poco):
    poco(text="会员卡").click()
    poco("com.caibaopay.cashier:id/tv_hint").click()

    touch(Template(r"images/2.png", record_pos=(0.305, 0.209), resolution=(1920, 1080)))
    touch(Template(r"images/5.png", record_pos=(0.305, 0.168), resolution=(1920, 1080)))

    touch(Template(r"images/6.png", record_pos=(0.379, 0.169), resolution=(1920, 1080)))
    touch(Template(r"images/1.png", record_pos=(0.231, 0.209), resolution=(1920, 1080)))
    touch(Template(r"images/yes.png", record_pos=(0.454, 0.232), resolution=(1920, 1080)))



