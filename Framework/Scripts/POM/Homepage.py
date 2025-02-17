from Scripts.Library.Lib import Wrapper
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from time import sleep
from selenium.common import exceptions

class HomePage(Wrapper):

    log_out_link=("xpath","//a[@class='ico-logout']")

    def __init__(self,driver):
        self.driver=driver

    def click_register(self):
        wrapper=Wrapper(self.driver)
        wrapper.click_item(("xpath","//a[@class='ico-register']"))

    def click_login(self):
        wrapper=Wrapper(self.driver)
        wrapper.click_item(("xpath","//a[.='Log in']"))



    def is_user_logged_in(self):
        for _ in range(5):
            try :
                self.driver.find_element(*self.log_out_link).is_displayed()
                return True
            except exceptions.NoSuchElementException:
                sleep(2)
                continue
        return False

