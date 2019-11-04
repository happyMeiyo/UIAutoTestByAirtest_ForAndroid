#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     userLogin
   Description :
   Author :        Meiyo
   date：          2019/10/9 10:44
-------------------------------------------------
   Change Activity:
                   2019/10/9:
------------------------------------------------- 
"""
__author__ = 'Meiyo'
from airtest.core.api import assert_not_equal


def user_login(poco, merchantcode, usercode, password):

    poco("com.caibaopay.cashier:id/et_company_account").set_text(merchantcode)
    poco("com.caibaopay.cashier:id/et_cashier_account").set_text(usercode)
    poco("com.caibaopay.cashier:id/et_pw").set_text(password)
    poco("com.caibaopay.cashier:id/tv_login").click()


def user_logout(poco):
    poco("com.caibaopay.cashier:id/ll_logout").wait_for_appearance(2)
    poco("com.caibaopay.cashier:id/ll_logout").click()




