from selenium import webdriver
import time
driver=webdriver.Chrome("E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")

driver.get("https://techwithtim.net")

print(driver.title)
time.sleep(2)



driver.quit()