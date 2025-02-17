from Scripts.Library.Lib import SeleniumWrapper
from selenium.common import exceptions
from time import sleep


class HomePage(SeleniumWrapper):
    login_link=("xpath","//a[@class='ico-login']")
    register_link=("xpath","//a[@class='ico-register']")
    log_out_link=("xpath","//a[@class='ico-logout']")


    def __init__(self,driver):
        self.driver=driver

    def click_register(self):
        wrapper=SeleniumWrapper(self.driver)
        wrapper.click_item(self.register_link)

    def click_login(self):
        wrapper=SeleniumWrapper(self.driver)
        wrapper.click_item(self.login_link)


    def is_user_logged_in(self):
        for _ in range(5):
            try:
                self.driver.find_element(*self.log_out_link).is_displayed()
                return True
            except exceptions.NoSuchElementException:
                sleep(2)
                continue
        return False















