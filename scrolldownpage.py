from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()
#scroll down page pixel
#driver.execute_script("window.scrollBy(0, 1000)", ""

flag=driver.find_element_by_xpath("//td[contains(text(),'India')]")
driver.execute_script("arguments[0].scrollIntoView();",flag)
