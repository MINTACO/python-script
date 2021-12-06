import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
# 后台运行
edge_options.add_argument('--start-maximized')
edge_options.use_chromium = True

driver = webdriver.Edge(service=edge_service, options=edge_options)

url = r'https://www.topuniversities.com/university-rankings/world-university-rankings/2022'

driver.get(url)

# cookie弹窗
wait = WebDriverWait(driver, 10)
cookie_accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/button')))
cookie_accept_button.click()
print('cookie accept button click')
sleep(2)

# 滚动到底部
driver.execute_script("window.scrollTo(0, 1600)")
print('window scrollTo(0, 1600)')

# 点击分页器
wait = WebDriverWait(driver, 10)
page_navigation = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div/div/div[3]/div[4]/div[1]/div[2]')))
page_navigation.click()
sleep(2)

# 选择每页个数100
driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div[4]').click()
print('select 100 each page')

# 获取uni list
sleep(8)
# 获取列表
list_of_universities = driver.find_elements(By.XPATH,
                                            '/html/body/div[1]/div/div/div[1]/div[2]/main/section/div/section/section/div/div/article/div/div[3]/div/div[1]/div/div[3]/div[1]/div[2]/*')

print('保存数据中...')
result = []

for index, uni in enumerate(list_of_universities):
    try:
        if 'need-section-margin' not in uni.get_attribute('class'):
            # print(uni.get_attribute('class'), type(uni.get_attribute('class')))
            name = uni.find_element(By.CLASS_NAME, 'uni-link').text
            website = uni.find_element(By.CLASS_NAME, 'uni-link').get_attribute('href')
            score = uni.find_element(By.CLASS_NAME, 'overall-score-span').text
            location = uni.find_element(By.CLASS_NAME, 'location').text
            temp = {
                'rank': index,
                'name': name,
                'overall_score': score,
                'website': website,
                'location': location
            }
            result.append(temp)
    except(RuntimeError, TypeError, ValueError):
        continue

with open('result1.json', 'w', encoding='utf-8') as json_file:
    # 有汉字要加上ensure_ascii=False
    json_file.write(json.dumps(result, indent=4, ensure_ascii=False))

print('All Done')

driver.quit()
# if __name__ == '__main__':
