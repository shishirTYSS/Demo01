from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import xlrd

def wait(some_func):
    def wrapper(*args,**kwargs):
        instance=args[0]
        locator=args[1]
        wait_=WebDriverWait(instance.driver,10)
        wait_.until(visibility_of_element_located(locator))
        return some_func(*args,**kwargs)
    return wrapper

class Wrapper:
    def __init__(self,driver):
        self.driver=driver

    @wait
    def click_item(self,locator):
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self,locator,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def select_item(self):
        pass



def read_locators(sheetname):
    wb=xlrd.open_workbook(r"C:\Users\SHISHIR\OneDrive\Desktop\Locators.xls")
    ws=wb.sheet_by_name(sheetname)
    used_rows=ws.nrows
    data={}
    for row_no in range(1,used_rows):
        temp_data=ws.row_values(row_no)
        data[temp_data[0]]=(temp_data[1],temp_data[2])
    return data











