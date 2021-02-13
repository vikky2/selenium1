from selenium import webdriver

driver=webdriver.Chromedriver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")

driver.get("https://www.yatra.com/")
driver.implicitly_wait(10)

#print(driver.title)


assert "Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com" in driver.title

#driver.find_element_by_xpath("//a[contains(text(),'My Account')]")

driver.find_element_by_xpath("//a[@title='Offers']").click()

# driver.find_element_by_css_selector("#login-input").send_keys("8386973745")
# driver.find_element_by_id("login-continue-btn").click()

driver.close()



