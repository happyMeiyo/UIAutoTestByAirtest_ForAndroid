#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     util
   Description :
   Author :        Meiyo
   date：          2019/10/9 11:27
-------------------------------------------------
   Change Activity:
                   2019/10/9:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import yaml
import io
import logging


def check_format(file_path, content):
    """ check testcase format if valid
    """
    if not content:
        # testcase file content is empty
        err_msg = u"Testcase file content is empty: {}".format(file_path)
        logging.error(err_msg)
        raise FileNotFoundError(err_msg)

    elif not isinstance(content, (list, dict)):
        # testcase file content does not match testcase format
        err_msg = u"Testcase file content format invalid: {}".format(file_path)
        logging.error(err_msg)
        raise FileNotFoundError(err_msg)


def load_yaml_file(yaml_file):
    """ load yaml file and check file content format
    """
    with io.open(yaml_file, 'r', encoding='utf-8') as stream:
        yaml_content = yaml.load(stream)
        check_format(yaml_file, yaml_content)
        return yaml_content