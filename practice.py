from selenium import webdriver
import unittest
import time
class GoogleSearchDemo(unittest.TestCase):
    def setUp(self):
        global driver
        driver=webdriver.Chrome("E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")
        driver.get("http://www.google.com")
        driver.maximize_window()

    def test(self):
        driver.find_element_by_name("q").send_keys("mahesh babu")
        time.sleep(2)
        driver.find_element_by_name('btnK').click()
        time.sleep(2)
        driver.find_element_by_name('LC201b').click()
        time.sleep(2)

    def tearDown(self):

        driver.close()



unittest.main()

