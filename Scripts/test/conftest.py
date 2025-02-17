from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from pytest import fixture
from Scripts.POM.Homepage import HomePage
from Scripts.POM.Loginpage import LoginPage


@fixture()
def driver():
    driver_=Chrome()
    driver_.get("https://demowebshop.tricentis.com/")
    driver_.maximize_window()
    yield driver_
    driver_.close()

@fixture()
def pages(driver):
    class Pages:
        homepage=HomePage(driver)
        loginpage=LoginPage(driver)
    return Pages()
