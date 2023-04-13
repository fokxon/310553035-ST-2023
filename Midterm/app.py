from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.edge.service import Service as EdgeService
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
#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://docs.python.org/3/tutorial/index.html")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/ul/li[7]/div[1]/select/option[9]'))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div')))
print(driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/section/h1').text)
print(driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/section/p[1]').text)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/ul/li[11]/div/form/input[1]'))).send_keys('class', Keys.RETURN)
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/ul/li')))
for i in range(1, 6):
    print(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/ul/li[' + str(i) + ']/a'))).text)
driver.quit()
