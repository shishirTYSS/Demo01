import openpyxl
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
opt=Options()
opt.add_experimental_option(name="detach",value=True)
driver=Chrome(opt)
# driver_=Firefox()
# sleep(5)
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
# sleep(5)
# driver.find_element("xpath","//input[@name='name']").send_keys("john")
# driver.maximize_window()
# driver.minimize_window()
# ele=driver.title
# print(ele)
# url=driver.current_url
# print(url)

# driver.get("https://demowebshop.tricentis.com/")
# elements=driver.find_elements("xpath","//div[@class='column customer-service']//li")
# for ele in elements:
#     print(ele.text)

# driver.get("https://www.python.org/downloads/")
# names=driver.find_elements("xpath","//ol[@class='list-row-container menu']//span[@class='release-number']")
# for name in names:
#     print(name.text)

# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element("xpath","//a[.='Build your own cheap computer']/../..//input[@value='Add to cart']").click()

# driver.get("file:///C:/Users/SHISHIR/OneDrive/Desktop/demo.html")
# dropdown=driver.find_element("xpath","//select[@id='multiple_cars']")
# select=Select(dropdown)
# select.select_by_visible_text("Toyota")
# sleep(2)
# select.select_by_index(3)
# sleep(2)
# select.select_by_value("hda")

# options=select.options
# for opt in options:
#     print(opt.text)

# dropdown_opt=[opt.text for opt in options]
# for item in dropdown_opt:
# #     select.select_by_visible_text(item)
# #     sleep(2)

# reversed_opt=dropdown_opt[::-1]
# for item in reversed_opt:
#     select.select_by_visible_text(item)
# select.deselect_by_visible_text("Audi")
# sleep(2)
# select.deselect_by_value("hda")
# sleep(2)
# select.deselect_by_index(5)
# sleep(2)
# select.deselect_all()

# for item in dropdown_opt:
#     if item=="Mercedes":
#         select.select_by_visible_text(item)

# driver.implicitly_wait(10)
# wait=WebDriverWait(driver,10)
# driver.get("file:///C:/Users/SHISHIR/OneDrive/Desktop/ajaxy_page%20(1).html")
# driver.find_element("xpath","//input[@name='typer']").send_keys("PYTHON")
# driver.find_element("xpath","//input[@id='green']").click()
# driver.find_element("xpath","//input[@name='submit']").click()
# element=("xpath","//div[@class='label']")
# wait.until(EC.visibility_of_element_located(element))
# print("Sucessfully Done")
