from Scripts.Library.Lib import SeleniumWrapper
from Scripts.POM.Homepage import HomePage


class LoginPage(HomePage):
    email_txtfld=("xpath","//input[@id='Email']")
    pwd_txtfld=("xpath","//input[@class='password']")
    login_btn=("xpath","//input[@class='button-1 login-button']")

    def login(self,email,password):
        wrapper=SeleniumWrapper(self.driver)
        wrapper.enter_text(self.email_txtfld,email)
        wrapper.enter_text(self.pwd_txtfld,password)
        wrapper.click_item(self.login_btn)

