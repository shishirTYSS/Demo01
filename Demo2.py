from selenium.webdriver.chrome.webdriver import WebDriver as Chrome

driver=Chrome()
driver.get("https://demowebshop.tricentis.com/")
elements=driver.find_elements("xpath","//div[@class='column customer-service']//a")
for element in elements:
    print(element.text)