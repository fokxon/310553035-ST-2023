from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.nycu.edu.tw/")
driver.maximize_window()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, '新聞'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'su-post'))).click()
print(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'entry-title'))).text)
for i in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'entry-content'))):
    print(i.text)

driver.switch_to.new_window('tab')
driver.get("https://www.google.com")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'gLFyf'))).send_keys('310553035', Keys.RETURN)
print(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'DKV0Md')))[1].text)
driver.quit()