from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://www.leafground.com/pages/Dropdown.html")

#Select the value in index 2
dropdown1 = Select(driver.find_element_by_id("dropdown1"))
dropdown1.select_by_index("2")

#Select the option with text 'Selenium'
dropdown2 = Select(driver.find_element_by_name("dropdown2"))
dropdown2.select_by_visible_text('Selenium')

#Select the option with value 3.
dropdown3 = Select(driver.find_element_by_name("dropdown3"))
dropdown3.select_by_value("3")

#count the number of options
dropdown4 = Select(driver.find_element_by_class_name("dropdown"))
print(len(dropdown4.options))

