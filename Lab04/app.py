from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://www.nycu.edu.tw/")
driver.maximize_window()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, '新聞'))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterForm"]/div/div[2]/div[1]'))).click()
print(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'subject'))).text)
for i in WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ed_txt'))):
    print(i.text)

driver.switch_to.new_window('tab')
driver.get("https://www.google.com")
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'gLFyf'))).send_keys('310553035', Keys.RETURN)
print(WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'DKV0Md')))[1].text)
driver.quit()
