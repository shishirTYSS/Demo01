from Scripts.Library.Lib import Wrapper
from Scripts.POM.Homepage import HomePage


class LoginPage(HomePage):

    def loginprocess(self):
        wrapper=Wrapper(self.driver)
        wrapper.enter_text(("xpath","//input[@name='Email']"),value="faizankhan@gmail.com")
        wrapper.enter_text(("xpath","//input[@class='password']"),value="123456")
        wrapper.click_item(("xpath","//input[@class='button-1 login-button']"))


