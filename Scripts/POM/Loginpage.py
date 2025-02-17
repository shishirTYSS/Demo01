from Scripts.POM.Homepage import HomePage
from Scripts.Library.Lib import Wrapper
from Scripts.Library.Lib import read_locators
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class LoginPage(HomePage):
    # email_txtfld=("xpath","//input[@class='email']")
    # pwd_txtfld=("xpath","//input[@id='Password']")
    # login_btn=("xpath","//input[@class='button-1 login-button']")
    login_fail_msg=("xpath","//div[@class='validation-summary-errors']")

    locator=read_locators("Loginpage")

    def login_process(self,email,password):
        wrapper=Wrapper(self.driver)
        wrapper.enter_text(self.locator["email_txtfld"],value=email)
        wrapper.enter_text(self.locator["pwd_txtfld"],value=password)
        wrapper.click_item(self.locator["login_btn"])

    def is_user_login_fail(self):
        for _ in range(5):
            try:
                self.driver.find_element(*self.login_fail_msg).is_displayed()
                return True
            except NoSuchElementException:
                sleep(2)
                continue
        return False



        