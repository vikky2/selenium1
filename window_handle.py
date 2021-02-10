from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")

driver.get("https://www.naukri.com/")
time.sleep(2)

win_handles=driver.window_handles
for handle in win_handles:
    driver.switch_to.window(handle)
    driver.close()
