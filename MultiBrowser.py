from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

driver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://www.google.com/")
time.sleep(1)

print(driver.title)

print(driver.current_url)
time.sleep(1)

print(driver.page_source) 










driver.close()

