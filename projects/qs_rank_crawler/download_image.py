#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonScript 
@File    ：download_image.py
@Author  ：Darren Lu
@Date    ：2021/12/5 
@Time    : 12:45
"""
import json
import requests


def main():
    f = open('qs_china_2.json', encoding='utf-8')
    # json.load将json对象转码为python对象， json.loads将json字符串转码为python对象
    data = json.load(f)

    image_url_list = [item['img_url'] for item in data]

    # print(image_url_list)
    for index, url in enumerate(image_url_list):
        file_name = str(data[index]["name"]) + '.jpg'

        response = requests.get(url)

        url_path = rf'university_pics\{file_name}'

        file = open(url_path, "wb")
        file.write(response.content)
        file.close()


if __name__ == '__main__':
    main()
