from selenium.webdriver.chrome.webdriver import WebDriver as Chrome

from Scripts.POM.Homepage import HomePage
from Scripts.POM.Loginpage import LoginPage

def test_Login(pages):
    pages.homepage.click_login()
    pages.loginpage.loginprocess()
    assert pages.homepage.is_user_logged_in() == True  # assert False == True

