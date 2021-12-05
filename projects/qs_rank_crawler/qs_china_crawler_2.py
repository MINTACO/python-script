#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonScript 
@File    ：qs_china_crawler_2.py
@Author  ：Darren Lu
@Date    ：2021/12/5 
@Time    : 10:26
"""
from init import init_driver
import json
from time import sleep
from selenium.webdriver.common.by import By

driver = init_driver()

f = open('qs_china_1.json', encoding='utf-8')

json1 = json.load(f)

# print(type(json1))

# print(json1[:3])
num = 1
#
result = [1, 2, 3]

for obj in json1:
    try:
        url = obj['website']
        driver.get(url)
        sleep(5)

        img_url = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/div/div/article/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[1]/a/img').get_attribute(
            'src')
        location = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/div/div/article/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]/p/span').text

        content_lis = driver.find_elements(By.XPATH,
                                           '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/div/div/article/div/div[1]/div/div[2]/div/div/div/ul/*')

        abouts = []
        for li in content_lis:
            content = li.find_element(By.TAG_NAME, 'span').text
            label = content.split('\n')[1]
            value = content.split('\n')[0]

            # value = li.find_element(By.CSS_SELECTOR, 'span>b').text
            temp_about = {
                'label': label,
                'value': value
            }
            abouts.append(temp_about)

        print(num, img_url, abouts)
        num += 1
        temp = dict(obj)

        temp['img_url'] = img_url
        temp['location'] = location
        temp['abouts'] = abouts

        result.append(temp)
    except:
        print('**************************')
        print(num)
        print('**************************')

        num += 1
        continue

with open('qs_china_2.json', 'w+', encoding='utf-8') as json_file:
    # 有汉字要加上ensure_ascii=False
    json_file.write(json.dumps(result, indent=4, ensure_ascii=False))

f.close()

print('All Done')

driver.quit()