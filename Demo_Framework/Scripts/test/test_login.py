from pytest import mark
from time import sleep
headers="email,password"
data=[("alice.scott@gmail1.com","alice@123"),
      ("bill.gates123@gmail1.com","bill@123")
      ]


@mark.parametrize(headers,data)
def test_Login(pages,email,password):
    pages.homepage.click_login()
    pages.loginpage.login(email,password)
    assert pages.homepage.is_user_logged_in() == True   # assert False == True
