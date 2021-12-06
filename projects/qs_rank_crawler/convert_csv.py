#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonScript 
@File    ：convert_csv.py
@Author  ：Darren Lu
@Date    ：2021/12/6 
@Time    : 22:33
"""
import json

f = open('final.json', encoding='utf-8')
# json.load将json对象转码为python对象， json.loads将json字符串转码为python对象
data = json.load(f)

with open('final_1.json', 'w+', encoding='utf-8') as json_file:
    for item in data:
        print(item)
        json_file.write(json.dumps(item, indent=4, ensure_ascii=False))

