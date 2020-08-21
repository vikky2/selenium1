from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/vikky/PycharmProjects/selenium/training/chromedriver')

driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")
time.sleep(3)

driver.find_element_by_link_text("Register").click()


time.sleep(1)

driver.find_element_by_name("FirstName").send_keys("Vikky")

driver.find_element_by_name("LastName").send_keys("Ranjan")

driver.find_element_by_id("register-button").click()






