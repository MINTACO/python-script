import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from time import sleep
import json

# 获取当前脚本的绝对路径
# print(os.path.abspath(__file__))
# 获取当前脚本的dir路径
# print(os.path.dirname(os.path.abspath(__file__)))

# DRIVER_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'browser_driver')
DRIVER_LOCATION = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'browser_driver')

# print(DRIVER_LOCATION)
# print(os.path.dirname(os.path.dirname(os.getcwd())))

CHROME_DRIVER_LOCATION = os.path.join(os.path.join(DRIVER_LOCATION, 'chromedriver_win32'), 'chromedriver.exe')
EDGE_DRIVER_LOCATION = os.path.join(os.path.join(DRIVER_LOCATION, 'edgedriver_win64'), 'msedgedriver.exe')

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')
# driver = webdriver.Chrome(executable_path=str(CHROME_DRIVER_LOCATION), options=chrome_options)

edge_service = EdgeService(executable_path=EDGE_DRIVER_LOCATION)

edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--start-maximized')
edge_options.use_chromium = True

driver = webdriver.Edge(service=edge_service, options=edge_options)

url = r'https://www.topuniversities.com/university-rankings/usa-rankings/2021'

driver.get(url)
sleep(10)

driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/button').click()
sleep(2)

driver.execute_script("window.scrollTo(0, 1600)")
sleep(3)
# 点击分页器
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[4]/div[1]/div[2]').click()
sleep(3)
# 点击个数100
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div[4]').click()
sleep(8)
# 获取列表
list_of_universities = driver.find_elements(By.XPATH,
                                           '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/*')

result = []

for uni in list_of_universities:
    try:
        rank = uni.find_element(By.CLASS_NAME, '_univ-rank').text
        name = uni.find_element(By.CLASS_NAME, 'uni-link').text
        website = uni.find_element(By.CLASS_NAME, 'uni-link').get_attribute('href')
        score = uni.find_element(By.CLASS_NAME, 'overall-score-span').text
        temp = {
            'name': name,
            'overall_score': score,
            'website': website
        }
        result.append(temp)
    except(RuntimeError, TypeError, NameError, ValueError):
        continue

with open('result1.json', 'w') as json_file:
    json.dump(result, json_file)

# if __name__ == '__main__':
