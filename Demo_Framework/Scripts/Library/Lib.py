from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(some_func):
    def wrapper(*args,**kwargs):
        instance=args[0]   #args=(self,locator)  args[0],args[1]
        locator_=args[1]
        wait_=WebDriverWait(instance.driver,10)
        wait_.until(EC.visibility_of_element_located(locator_))
        return some_func(*args,**kwargs)
    return wrapper


class SeleniumWrapper:

    def __init__(self,driver):
        self.driver=driver

    @wait
    def click_item(self,locator):
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)


