#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonScript 
@File    ：convert_json.py
@Author  ：Darren Lu
@Date    ：2021/12/6 
@Time    : 22:12
"""

import json

f1 = open('result1.json', encoding='utf-8')
# json.load将json对象转码为python对象， json.loads将json字符串转码为python对象
data1 = json.load(f1)

f2 = open('qs_china_2.json', encoding='utf-8')
# json.load将json对象转码为python对象， json.loads将json字符串转码为python对象
data2 = json.load(f2)

print(len(data1), len(data2))

for index, item in enumerate(data1):
    data2[index]['en_name'] = item['name']

with open('final.json', 'w+', encoding='utf-8') as json_file:
    # 有汉字要加上ensure_ascii=False
    json_file.write(json.dumps(data2, indent=4, ensure_ascii=False))

f1.close()
f2.close()

