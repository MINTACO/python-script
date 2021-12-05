#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonScript 
@File    ：qs_china_crawler1.py.py
@Author  ：Darren Lu
@Date    ：2021/12/4 
@Time    : 8:57
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json
from init import init_driver


url = r'https://www.qschina.cn/university-rankings/world-university-rankings/2022'

driver = init_driver()

driver.get(url)

# cookie弹窗
sleep(8)

driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/button[2]').click()
print('cookie accept button click')
sleep(2)

# 滚动到底部
driver.execute_script("window.scrollTo(0, 2600)")
print('window scrollTo(0, 2600)')

# 点击分页器
wait = WebDriverWait(driver, 10)
page_navigation = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/div/div/article/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/div[1]/label/span[2]')))
page_navigation.click()
sleep(2)

# 选择每页个数100
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/div/div/article/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/div[1]/label/span[2]/div/div/span/span/ul/li[3]/span').click()
print('select 100 each page')

# 获取uni list
sleep(8)
# 获取列表
list_of_universities = driver.find_elements(By.XPATH,
                                            '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/div/div/article/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/table/tbody/*')

print('保存数据中...')
result = []

for uni in list_of_universities:
    try:
        if 'in-ad' not in uni.get_attribute('class'):
            # print(uni.get_attribute('class'), type(uni.get_attribute('class')))
            rank = uni.find_element(By.CSS_SELECTOR, 'td.rank>div').text
            name = uni.find_element(By.CLASS_NAME, 'uni-link').text
            website = uni.find_element(By.CLASS_NAME, 'uni-link').get_attribute('href')
            # score = uni.find_element(By.CLASS_NAME, 'overall-score-span').text
            nation = uni.find_element(By.CLASS_NAME, 'location').text
            temp = {
                'rank': rank,
                'name': name,
                # 'overall_score': score,
                'website': website,
                'nation': nation
            }
            result.append(temp)
    except(RuntimeError, TypeError, ValueError):
        continue

with open('qs_china_1.json', 'w', encoding='utf-8') as json_file:
    # 有汉字要加上ensure_ascii=False
    json_file.write(json.dumps(result, indent=4, ensure_ascii=False))

print('All Done')

driver.quit()
# if __name__ == '__main__':
