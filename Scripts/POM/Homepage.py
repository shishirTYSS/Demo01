from Scripts.Library.Lib import Wrapper



class HomePage(Wrapper):

    login_link=("xpath","//a[@class='ico-login']")

    def __int__(self,driver):
        self.driver=driver

    def click_login(self):
        wrapper=Wrapper(self.driver)
        wrapper.click_item(self.login_link)






