from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://docs.python.org/3/tutorial/index.html")
driver.maximize_window()
print(WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div [class="body"]')))[0].text)
print(WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div [class="body"] p')))[0].text)
#WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'option[value="zh-tw"]'))).click()

"""
print(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'single-post-title'))).text)
for i in WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'entry-content'))):
    print(i.text)

driver.switch_to.new_window('tab')
driver.get("https://www.google.com")
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'gLFyf'))).send_keys('310553035', Keys.RETURN)
print(WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'DKV0Md')))[1].text)
driver.quit()
"""