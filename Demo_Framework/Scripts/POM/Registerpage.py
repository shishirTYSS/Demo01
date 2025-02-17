from socket import errorTab

from Scripts.Library.Lib import SeleniumWrapper
from Scripts.POM.Homepage import HomePage


class RegisterPage(HomePage):

    gender_rdo_btn=("xpath","//input[@id='gender-male']")
    frst_name_txtfld=("xpath","//input[@id='FirstName']")
    lst_name_txtfld=("xpath","//input[@name='LastName']")
    email_txtfld=("xpath","//input[@id='Email']")
    pwd_txtfld=("xpath","//input[@id='Password']")
    cnfrm_pwd_txtfld=("xpath","//input[@name='ConfirmPassword']")
    register_btn=("xpath","//input[@name='register-button']")

    def register_process(self,fname,lname,email,pwd,cnfpwd):
        wrapper=SeleniumWrapper(self.driver)
        wrapper.click_item(self.gender_rdo_btn)
        wrapper.enter_text(self.frst_name_txtfld,fname)
        wrapper.enter_text(self.lst_name_txtfld,lname)
        wrapper.enter_text(self.email_txtfld,email)
        wrapper.enter_text(self.pwd_txtfld,pwd)
        wrapper.enter_text(self.cnfrm_pwd_txtfld,cnfpwd)
        wrapper.click_item(self.register_btn)