from selenium import webdriver
from time import sleep

driver=webdriver.Chrome("E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")
driver.get("https://www.amazon.in/")
#driver.get("https://www.ndtv.com/")
sleep(5)

driver.find_element_by_xpath("(//span[text()='Bedsheets, curtains & more'])[1]").click()



