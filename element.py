from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/vikky/PycharmProjects/selenium/training/chromedriver')

driver.maximize_window()
driver.get('http://demowebshop.tricentis.com/')

time.sleep(2)

images=driver.find_elements_by_xpath("//img")
print('Total Images on the page:',len(images))
time.sleep(1)
driver.quit()






