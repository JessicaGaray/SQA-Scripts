from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
searchbar = driver.find_element_by_name("q")
searchbar.clear()
searchbar.send_keys("iacademy")
searchbar.send_keys(Keys.RETURN)

links = driver.find_elements_by_tag_name("a")
print(len(links))