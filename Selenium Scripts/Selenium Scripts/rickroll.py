from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
driver.save_screenshot('youtube.jpeg')
search = driver.find_element_by_name("search_query")
search.clear()
search.send_keys("Rick Astley")
driver.save_screenshot('search-rick-astley.jpg')
search.send_keys(Keys.RETURN)
driver.implicitly_wait(20)
driver.save_screenshot('search-results.jpeg')
video = driver.find_element_by_partial_link_text("Never Gonna Give You Up")
video.click()
driver.implicitly_wait(30)
driver.save_screenshot('rickroll.jpeg')