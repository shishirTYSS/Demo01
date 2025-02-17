from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from Scripts.POM.Homepage import HomePage
from Scripts.POM.Loginpage import LoginPage
from time import sleep
from pytest import mark

headers="email,password"
data=[
    ("abc@gmail.com","12345678"),
    ("def@gmail.com","123456789"),
    ("xyz@gmail.com","2468"),
]

@mark.parametrize(headers,data)
def test_login(pages,email,password):
    pages.homepage.click_login()
    pages.loginpage.login_process(email,password)
    assert pages.loginpage.is_user_login_fail() == True


