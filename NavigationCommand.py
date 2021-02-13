from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chromedriver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")

driver.get("https://www.yatra.com/")
print(driver.title)
time.sleep(1)

driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)
time.sleep(1)

driver.back()

print(driver.title)
time.sleep(1)

driver.forward()

print(driver.title)

driver.close()
