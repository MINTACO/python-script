from projects.excel2json import excel2json
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 获取当前脚本的绝对路径
# print(os.path.abspath(__file__))
# 获取当前脚本的dir路径
# print(os.path.dirname(os.path.abspath(__file__)))

DRIVER_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'browser_driver')

CHROME_DRIVER_LOCATION = os.path.join(os.path.join(DRIVER_LOCATION, 'chromedriver_win32'), 'chromedriver.exe')
EDGE_DRIVER_LOCATION = os.path.join(os.path.join(DRIVER_LOCATION, 'edgedriver_win64'), 'msedgedriver.exe')

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')
# driver = webdriver.Chrome(executable_path=str(CHROME_DRIVER_LOCATION), options=chrome_options)

edge_service = Service(EDGE_DRIVER_LOCATION)

edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--start-maximized')
edge_options.use_chromium = True

driver = webdriver.Edge(service=edge_service, options=edge_options)

driver.get('https://www.baidu.com')

# search_text = driver.find_element_by_id('kw')
# search_text.send_keys('selenium')
# search_text.submit()
