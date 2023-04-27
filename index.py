import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import shutil

url = "https://dzaadg8s4xglo.cloudfront.net"

with Chrome() as driver:
    driver.get(url)

folder_name = "data"
file_name = "index.json"

emailLogin = "loc.tran+30@arent3d.com"
passwordLogin = "Aa@123456"

if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
else:
    print("Folder is not exist")

os.makedirs(folder_name)

f = open(os.path.join(folder_name, file_name), "w")
f.close()

email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

email_input.send_keys(emailLogin)
password_input.send_keys(passwordLogin)
time.sleep(2)
submit_button.click()

time.sleep(10)

table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
)

rows = []
for row in table.find_elements(By.CSS_SELECTOR, "tr"):
    cells = []
    for cell in row.find_elements(By.CSS_SELECTOR, "td"):
        cells.append(cell.text)
    rows.append(cells)

with open("./data/index.json", "w") as outfile:
    json.dump(rows, outfile, ensure_ascii=False)

driver.quit()
