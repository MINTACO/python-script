#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonScript 
@File    ：init.py
@Author  ：Darren Lu
@Date    ：2021/12/4 
@Time    : 8:59
"""

import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService


DRIVER_LOCATION = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'browser_driver')

CHROME_DRIVER_LOCATION = os.path.join(os.path.join(DRIVER_LOCATION, 'chromedriver_win32'), 'chromedriver.exe')
EDGE_DRIVER_LOCATION = os.path.join(os.path.join(DRIVER_LOCATION, 'edgedriver_win64'), 'msedgedriver.exe')

# DRIVER_DICT = {
#
# }


def init_driver():
    edge_service = EdgeService(executable_path=EDGE_DRIVER_LOCATION)

    edge_options = webdriver.EdgeOptions()
    # 后台运行
    edge_options.add_argument('--start-maximized')
    edge_options.use_chromium = True

    driver = webdriver.Edge(service=edge_service, options=edge_options)

    return driver

