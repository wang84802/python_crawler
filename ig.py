from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import wget
import time
import config as config

PATH = 'C:/Users/Gaming/Desktop/python/crawl/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')

#出現username標籤才執行
username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
username.clear()
password.clear()
ig_username = config.ig_username # 帳號
ig_password = config.ig_password # 密碼
username.send_keys(ig_username)
password.send_keys(ig_password)
actions = ActionChains(driver)
login.click()

search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    )
keyword = '#cat'
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    )

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

imgs = driver.find_elements(By.CLASS_NAME, 'FFVAD')
path_download = os.path.join(keyword)
now = time.time()
path_download = path_download + '_' + str(round(now))

os.mkdir(path_download)

count = 0
for img in imgs:
    save_as = os.path.join(path_download, keyword + str(count) + '.jpg')
    wget.download(img.get_attribute('src'), save_as)
    count += 1
