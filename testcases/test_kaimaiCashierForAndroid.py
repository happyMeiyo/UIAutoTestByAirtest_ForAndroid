#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     test_kaimaiCashierForAndroid
   Description :
   Author :        Meiyo
   date：          2019/10/10 16:08
-------------------------------------------------
   Change Activity:
                   2019/10/10:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import sys

# sys.path.append("E:/xiaohexian_project/UItest_for_cashier")

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from api.userLogin import user_login, user_logout
from api.goods import goods_add_shopping_cart
from api.vip import search_vip
from api.keyboardcode import input_keyboard_code
from util import load_yaml_file
import unittest


class CashierForAndroidCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect_device("Android://127.0.0.1:5037/DA08196340368")

        start_app('com.caibaopay.cashier')

        cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def setUp(self):
        content = load_yaml_file(os.getcwd() + '/config/cashier.yml')
        user_info = content.get('ShopManagerInfo')
        merchant_code = user_info['merchantcode']
        user_code = user_info['usercode']
        password = user_info['password']

        user_login(self.poco, merchant_code, user_code, password)

        self.poco("com.caibaopay.cashier:id/ll_logout").wait_for_appearance(2)
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_shop_info").exists(), True, "登录成功")

    def tearDown(self):
        user_logout(self.poco)

    def test_pendingAndGetOrder(self):
        # %% 挂单
        # 加购商品
        self.poco(text="哈密瓜切果").click()
        self.poco(text="劲霸汤皇").click()

        # 切换类目
        self.poco(text="其他水果").click()

        # 加购商品
        self.poco(text="草莓味水果捞").click()
        self.poco("com.caibaopay.cashier:id/rl_take_order").click()

        assert_equal(self.poco("com.caibaopay.cashier:id/tv_take_order").get_text(), "取单", "挂单成功.")
        # %%

        # %% 取单列表
        self.poco("com.caibaopay.cashier:id/rl_take_order").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/ftv_amount").get_text(), "24.00", "显示挂单列表成功.")
        # %%

        # %% 取单
        self.poco("android.widget.LinearLayout").offspring("android:id/content").child(
            "android.widget.LinearLayout").offspring("com.caibaopay.cashier:id/fl_container").child(
            "android.widget.LinearLayout").offspring("com.caibaopay.cashier:id/fl_right").offspring(
            "com.caibaopay.cashier:id/rlv_order_list").child("com.caibaopay.cashier:id/ll_root").child(
            "android.widget.LinearLayout").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/ltv_total_discount_price").get_text(), "24.00", "取单成功.")
        # %%

        # %% 清除购物车
        self.poco("com.caibaopay.cashier:id/ll_delete_all").click()
        self.poco("com.caibaopay.cashier:id/tv_confirm").wait_for_appearance(1)
        self.poco("com.caibaopay.cashier:id/tv_confirm").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_cart_info").get_text(), "购物车为空", "清空购物车成功")
        # %%

    def test_temporaryGoods(self):

        # %% 选择临时商品，计件
        self.poco("com.caibaopay.cashier:id/rl_parent_category").wait_for_appearance(2)
        self.poco(text="冷藏酸奶").swipe([-0.5712, 0.0439])
        self.poco(text="临时商品").click()
        self.poco(text="临时商品_计件").click()
        # %%

        # %% 设置临时商品的零售价（5）和数量（3）
        self.poco("com.caibaopay.cashier:id/view_keyboard").wait_for_appearance(2)
        self.poco("com.caibaopay.cashier:id/tv_sale_price").click()
        input_keyboard_code(5)

        self.poco("com.caibaopay.cashier:id/tv_number").click()
        input_keyboard_code(2)
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_total_price").get_text(), "10.00", "输入零售价和数量成功")
        # %%

        # %% 加入购物车
        self.poco("com.caibaopay.cashier:id/tv_confirm").click()
        self.poco("com.caibaopay.cashier:id/ll_go_cash").wait_for_appearance(2)
        assert_equal(self.poco("com.caibaopay.cashier:id/ltv_total_discount_price").get_text(), "10.00", "临时商品加购成功")
        # %%

    def test_payByVipCard(self):
        # %% 商品加购
        goods_add_shopping_cart(self.poco)
        # %%

        self.poco("com.caibaopay.cashier:id/ll_go_cash").click()

        # %% 搜索会员
        self.poco(text="会员卡").click()
        self.poco("com.caibaopay.cashier:id/tv_hint").click()
        search_vip(self.poco)
        self.poco("com.caibaopay.cashier:id/rl_vip_member").wait_for_appearance(2)
        self.poco(text="文心").click()
        # %%

        # %% 选择积分抵扣
        self.poco("com.caibaopay.cashier:id/ll_use_integral").wait_for_appearance(2)
        self.poco("com.caibaopay.cashier:id/ll_use_integral").click()
        input_keyboard_code(8)
        input_keyboard_code("yes")
        # %%

        # %% 整单优惠
        self.poco("com.caibaopay.cashier:id/tv_whole_discount").click()
        input_keyboard_code(1)
        input_keyboard_code(0)
        input_keyboard_code("yes")
        # %%

        # %% 会员支付
        self.poco("com.caibaopay.cashier:id/tv_confirm_pay").click()
        # self.poco("com.caibaopay.cashier:id/action_bar_root").wait_for_appearance(2)
        # assert_equal(self.poco("com.caibaopay.cashier:id/tv_tip").get_text(), "支付成功", "会员支付成功.")
        # %%

    def test_payByCash(self):
        # %% 商品加购
        goods_add_shopping_cart(self.poco)
        # %%

        # %% 现金支付
        self.poco("com.caibaopay.cashier:id/ll_go_cash").click()
        self.poco(text="现金&记账").click()

        self.poco("com.caibaopay.cashier:id/tv_fourth").click()

        self.poco("com.caibaopay.cashier:id/ll_cash_back").wait_for_appearance(2)

        assert_not_equal(self.poco("com.caibaopay.cashier:id/atv_cash_back").get_text(), "0.00", "找零金额不为0.")

        input_keyboard_code("yesforpay")

        # self.poco("com.caibaopay.cashier:id/action_bar_root").wait_for_appearance(2)
        # assert_equal(self.poco("com.caibaopay.cashier:id/tv_tip").get_text(), "支付成功", "现金支付成功.")
        # %%

    def test_payByBarcode(self):
        # %% 商品加购
        goods_add_shopping_cart(self.poco)
        # %%

        # %% 输入二维码
        self.poco("com.caibaopay.cashier:id/ll_go_cash").click()
        self.poco(text="扫码支付").click()

        self.poco("com.caibaopay.cashier:id/tv_input_code").click()

        input_keyboard_code(5)
        input_keyboard_code(5)
        input_keyboard_code(5)
        input_keyboard_code(5)
        input_keyboard_code(0)
        input_keyboard_code(1)
        input_keyboard_code(2)
        input_keyboard_code(3)
        input_keyboard_code(4)
        input_keyboard_code(5)
        input_keyboard_code(6)
        input_keyboard_code(7)
        input_keyboard_code(8)
        input_keyboard_code(9)
        # %%

        # %% 支付失败
        input_keyboard_code("yesforpay")

        self.poco("com.caibaopay.cashier:id/ll_error").wait_for_appearance(2)
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_error_msg").get_text(),
                     "无效的付款条码，请扫描消费者手机付款条码重试！",  "扫码支付失败")

        self.poco("com.caibaopay.cashier:id/tv_account").click()
        self.poco("com.caibaopay.cashier:id/rl_order_list").wait_for_appearance(2)
        assert_equal(self.poco("com.caibaopay.cashier:id/rl_order_list")
                     .child("com.caibaopay.cashier:id/ll_order_container")[0]
                     .offspring("com.caibaopay.cashier:id/tv_order_state").get_text(), "待收款", "订单状态是未收款")

        # %%

    def test_chargeByCash(self):
        # %% 搜索会员
        self.poco(text="会员").click()
        self.poco(text="手机号码 / 会员码").click()
        search_vip(self.poco)
        self.poco(text="哈哈").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_vip_name").get_text(), "哈哈", "查询会员成功.")
        # %%

        # %% 充值
        self.poco("com.caibaopay.cashier:id/rl_balance").click()
        self.poco(text="自定义金额").click()
        input_keyboard_code(1)
        input_keyboard_code(0)
        input_keyboard_code("yes")
        self.poco(text="现金支付").click()
        self.poco("com.caibaopay.cashier:id/tv_confirm_pay").click()

        self.poco("com.caibaopay.cashier:id/custom").wait_for_appearance(15)
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_recharge_amount").get_text(), "10.00", "充值成功")
        self.poco("com.caibaopay.cashier:id/tv_confirm").click()
        # %%

    def test_queryCouponAndPoint(self):
        # %% 搜索会员
        self.poco(text="会员").click()
        self.poco(text="手机号码 / 会员码").click()
        search_vip(self.poco)
        self.poco(text="文心").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_vip_name").get_text(), "文心", "查询会员成功.")
        # %%

        self.poco("com.caibaopay.cashier:id/rl_coupon").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/fl_right")
                     .offspring("com.caibaopay.cashier:id/rl_coupon").exists(),
                     True, "查看券列表成功")

        self.poco("com.caibaopay.cashier:id/rl_point").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/rl_point_list").exists(), True, "查看积分列表成功")

    def test_bandAndUnbandCard(self):
        # %% 搜索会员
        self.poco(text="会员").click()
        self.poco(text="手机号码 / 会员码").click()
        search_vip(self.poco)
        self.poco(text="文心").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/tv_vip_name").get_text(), "文心", "查询会员成功.")
        # %%

        self.poco("com.caibaopay.cashier:id/rl_physical_card").click()
        self.poco(text="实体卡卡号").click()

        input_keyboard_code(1)
        input_keyboard_code(2)
        input_keyboard_code(3)
        input_keyboard_code(4)
        input_keyboard_code(5)
        input_keyboard_code(6)
        input_keyboard_code(7)
        input_keyboard_code(8)
        input_keyboard_code(9)
        input_keyboard_code(0)
        input_keyboard_code("yes")

        assert_equal(self.poco("com.caibaopay.cashier:id/aft_physical_card").get_text(), "1234567890", "绑卡成功.")
        self.poco("com.caibaopay.cashier:id/tv_unbind").click()
        assert_equal(self.poco("com.caibaopay.cashier:id/aft_physical_card").get_text(), "尚未绑定实体卡", "解绑成功.")
