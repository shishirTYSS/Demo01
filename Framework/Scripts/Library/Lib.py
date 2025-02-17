from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait(some_func):
    def wrapper(*args,**kwargs):
        instance=args[0]
        locator=args[1]
        wait_=WebDriverWait(instance.driver,10)
        wait_.until(EC.visibility_of_element_located(locator))
        return some_func(*args,**kwargs)
    return wrapper


class Wrapper:
    def __init__(self,driver):
        self.driver=driver

    @wait
    def click_item(self,locator):
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self,locator,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)


    def select_item(self):
        pass

    def mouse_hover(self):
        pass

