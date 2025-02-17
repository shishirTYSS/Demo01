from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from Scripts.POM.Homepage import HomePage
from Scripts.POM.Registerpage import RegisterPage
from pytest import mark

headers="fname,lname,email,pwd,cnfpwd"
data=[("Alice","Scott","alice.scott@gmail.com","alice@123","alice@123"),
      ("Bill","Gates","bill.gates123@gmail.com","bill@123","bill@123"),
      ("Sachin","tendulkar","sachin@gmail.com","sac123","sac123"),
      ("Charan","Kumar","charan.kumar@gmail.com","char123","char123")
      ]

@mark.parametrize(headers,data)
def test_Register(pages,fname,lname,email,pwd,cnfpwd):
    pages.homepage.click_register()
    pages.registerpage.register_process(fname,lname,email,pwd,cnfpwd)
