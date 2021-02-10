from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("https://mail.google.com/mail/u/0/#all/FMfcgxwLsKDGRSxcQdXRtMNTGfmdqFdJ")
driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys("Vikky Ranjan")
time.sleep(1)