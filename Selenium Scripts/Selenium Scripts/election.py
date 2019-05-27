from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.get('http://www.google.com')
driver.save_screenshot('google.jpeg')
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("rappler senatorial election result 2019")
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(20)
driver.save_screenshot('search-results.jpeg')
results = driver.find_element_by_class_name("LC20lb")
results.click()
driver.implicitly_wait(20)
driver.save_screenshot('rappler-page.jpeg')

task = driver.find_element_by_id("story-area-230703")
senatorlist = task.find_element_by_tag_name("ol")
senators = senatorlist.find_elements_by_tag_name("li")
    
for i in senators:
    print(i.text)
    
