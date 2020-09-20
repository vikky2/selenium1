from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
import time

driver=webdriver.Chrome("E:\Softy $ Drivers\chromedriver_win32/chromedriver.exe")
driver.get("file:///C:/Users/vikky/Desktop/HTML%20Pages/javascript.html")
driver.get("http://demowebshop.tricentis.com/")

class element_visibility_and_enabled:
    def __init__(self, locator):
        self.locator=locator
    def __call__(self, driven):
        loctype, locvalue=self.locator
        element=driver.find_element(loctype, locvalue)
        if element.is_enabled() and element.is_displayed():
            return True
        else:
            return False
    def element_to_be_visible_enabled(locator):
        def wrapper(driven):
            loctype, locvalue=locator
            element=driver.find_element(loctype, locvalue)
            if element.is_displayed() and element.is_enabled():
                return True
            else:
                return False
        return wrapper

    MAX_TIMEOUT= 60

    def _wait(*, visible=True, enabled=True, max_timeout=10, is_alert=False):
     def _wait(*, visible=True, enabled=True, is_alert=False):

            def decorate(func):
                w=WebDriverWait(driver, max_timeout)
                w=WebDriverWait(driver, MAX_TIMEOUT)
                def wrapper(*args, **kwargs):
                    locator, =args
                    if visible and enabled and not is_alert:
                       w.until(element_visibility_and_enabled(locator))
                    elif visible and not enabled and not is_alert:
                        w.until(ec.visibility_of_element_located(locator))
                    elif not visible and not is_alert:
                        w.until(ec.invisibility_of_element_located(locator))
                    elif is_alert:
                        w.until(ec.alert_is_present)
                    return func(*args, **kwargs)
                return wrapper
            return decorate
     @_wait(max_timeout=3)
     @_wait()
     def enter_text(locator, *, value):
         locatortype, locatorvalue= locator
         driver.find_element(locatortype, locatorvalue).clear()
         driver.find_elements(locatortype, locatorvalue).send_keys(value)

     @_wait(is_alert=True)
     @_wait()
     def click_element(locator):
         locatortype, locatorvalue=locator
         driver.find_element(locatortype, locatorvalue).click()

     @_wait(max_timeout=8)
     @_wait()
     def select_item(locator, *, item):
         loactortype, locatorvalue=locator
         lst_box= driver.find_element(loactortype, locatorvalue)
         s=Select(lst_box)
         items=[opt.text for opt in s.options]
         if isinstance(item, str):
             if item not in items:
                 raise ValueError(f'{item}not found in the list')
             s.select_by_visible_text(item)
         else:
             if item>len(items):
                 raise IndexError('Index Error')
             s.select_by_index(item)

             @_wait()
             def select_items(locator, *, items):
                 for item in items:
                     try:
                         select_item(locator, item=item)
                         time.sleep(1)
                     except(ValueError, IndexError):
                         print(f'{item}was not found in the miulti select listbox')
                         continue


                         driver.switch_to.frame()
                         driver.switch_to.default_content()
                         driver.switch_to.parent_frame()
                         click_element(("xpath", "//a[text()='Register']"))
                         click_element(('id', 'gender-male'))
                         enter_text(("name", "FirstName"), value="Sandeep")
                         enter_text(("name", "Lastname"), value="Suryaprasad")
                         click_element(("id", "register-button"))

















