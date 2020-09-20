from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome("E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")
driver.get("file:///C:/Users/vikky/Desktop/HTML%20Pages/Mouse_hover.html")

time.sleep(2)
menus=['About', 'Blog', 'Projects', 'Contact']
actions=ActionChains(driver)
for menu in menus:
    menu_xpath=f"//a[text()='{menu}']"
    element=driver.find_element_by_xpath(menu_xpath)
    actions.move_to_element(element).perform()
    time.sleep(2)
















