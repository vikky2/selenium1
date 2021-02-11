from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")

driver.get("https://www.rapidvaluesolutions.com/automation-testing-vs-manual-testing/")
#driver.save_screenshot("C:\Screenshot\homepage.png")

#another way to capture screeenshot in selenium
driver.get_screenshot_as_file("C:\Screenshot\homepage2.jpg")
