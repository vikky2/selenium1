from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()
#scroll down page pixel
driver.execute_script("window.scrollBy(0, 1000)", "")
