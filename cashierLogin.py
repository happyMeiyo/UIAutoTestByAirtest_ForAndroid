#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     cashierLogin
   Description :
   Author :        Meiyo
   date：          2019/9/26 10:26
-------------------------------------------------
   Change Activity:
                   2019/9/26:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco("com.caibaopay.cashier:id/et_company_account").set_text("101993")
poco("com.caibaopay.cashier:id/et_cashier_account").set_text("qing")
poco("com.caibaopay.cashier:id/et_pw").set_text("a123456")
poco("com.caibaopay.cashier:id/tv_login").click()


assert_equal(poco("com.caibaopay.cashier:id/tv_shop_info").get_text(),
             "您好 ！清，欢迎来到开麦，登录门店：合言运营商户/清雨的门店", "登录的收银员与门店正确.")



