#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     goods
   Description :
   Author :        Meiyo
   date：          2019/10/23 15:23
-------------------------------------------------
   Change Activity:
                   2019/10/23:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

from airtest.core.api import assert_equal


def goods_add_shopping_cart(poco):
    poco("com.caibaopay.cashier:id/fl_right").wait_for_appearance(10)

    poco(text="海天 蒸鱼鼓油 450ml").click()

    poco(text="红玫瑰苹果").click()

    poco("com.caibaopay.cashier:id/rl_product").swipe([0.0337, -0.5722])
    poco("com.caibaopay.cashier:id/rl_product").swipe([0.0202, -0.4884])

    poco(text="烟台苹果 箱").click()

    poco(text="秋香苹果").click()

    assert_equal(poco("com.caibaopay.cashier:id/fl_left").child("android.widget.FrameLayout").offspring(
        "com.caibaopay.cashier:id/rv_product").child("com.caibaopay.cashier:id/ll_container")[0].offspring(
        "com.caibaopay.cashier:id/tv_order_number").get_text(), "4", "购物车加购成功")


