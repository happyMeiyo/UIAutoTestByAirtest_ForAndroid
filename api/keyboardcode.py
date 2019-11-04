#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     keyboardcode
   Description :
   Author :        Meiyo
   date：          2019/10/24 11:11
------------------------------------------------（-
   Change Activity:
                   2019/10/24:
------------------------------------------------- 
"""
__author__ = 'Meiyo'
from airtest.core.api import touch, Template


def input_keyboard_code(code, record_pos=None, resolution=(1920, 1080)):

    if code == 0:
        record_pos = (0.268, 0.25)
    elif code == 1:
        record_pos = (0.231, 0.21)
    elif code == 2:
        record_pos = (0.304, 0.209)
    elif code == 3:
        record_pos = (0.379, 0.21)
    elif code == 4:
        record_pos = (0.23, 0.17)
    elif code == 5:
        record_pos = (0.305, 0.169)
    elif code == 6:
        record_pos = (0.379, 0.17)
    elif code == 7:
        record_pos = (0.229, 0.131)
    elif code == 8:
        record_pos = (0.304, 0.131)
    elif code == 9:
        record_pos = (0.379, 0.131)
    elif code == "dot":
        record_pos=(0.379, 0.251)
    elif code == "yesforpay":
        record_pos = (0.379, 0.249)
    elif code == "yes":
        record_pos = (0.453, 0.229)

    touch(Template(r"images/" + str(code) + r".png", threshold=0.5, record_pos=record_pos, resolution=resolution))