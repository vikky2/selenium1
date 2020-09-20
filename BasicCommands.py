from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://www.yatra.com")
print(driver.title)

driver.get("http://www.fb.com/")
print(driver.title)
time.sleep(1)

driver.back()
time.sleep(1)

print(driver.title)

driver.forward()
time.sleep(1)

print(driver.title)



time.sleep(2)



driver.close()