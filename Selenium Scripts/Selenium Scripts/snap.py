from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("thanos")
elem.send_keys(Keys.RETURN)
gauntlet = driver.find_element_by_class_name("Z4Kand")
gauntlet.click()
assert "No results found." not in driver.page_source