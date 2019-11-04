#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     test_kaimaiLogin
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
sys.path.append("E:/xiaohexian_project/UItest_for_cashier")

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from api.userLogin import user_login, user_logout
from util import load_yaml_file
import unittest


class UserLoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("custom setup")
        # add var/function/class/.. to globals
        # self.scope["hunter"] = "i am hunter"
        # self.scope["add"] = lambda x: x+1

        # exec setup script
        connect_device("Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP&ori_method=ADBORI")

        cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def setUp(self):
        content = load_yaml_file(os.getcwd() + '/config/cashier.yml')
        user_info = content.get('ShopManagerInfo')
        merchant_code = user_info['merchantcode']
        user_code = user_info['usercode']
        password = user_info['password']

        user_login(self.poco, merchant_code, user_code, password)

    def tearDown(self):
        user_logout(self.poco)

    def test_temporaryGoods(self):
        # %% 加购临时商品

        self.poco(text="临时商品").swipe([-0.5712, 0.0439])
        self.poco(text="临时商品").click()
        self.poco(text="临时商品_计件").click()

        time.sleep(2)

        print(self.poco("com.caibaopay.cashier:id/tv_sale_price").get_text())

        self.poco("com.caibaopay.cashier:id/tv_sale_price").set_text("12")

        print(self.poco("com.caibaopay.cashier:id/tv_number").get_text())

        self.poco("com.caibaopay.cashier:id/tv_number").set_text("5")

        self.poco("com.caibaopay.cashier:id/tv_confirm").click()

        # %%


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UserLoginTestCase))

    result = unittest.TextTestRunner(verbosity=0).run(suite)
