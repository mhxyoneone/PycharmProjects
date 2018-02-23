from selenium import webdriver
driver = webdriver.PhantomJS(executable_path=r'C:\Users\Kevin\PycharmProjects\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("######")
print(driver.find_element_by_id('magnet-table').text)

