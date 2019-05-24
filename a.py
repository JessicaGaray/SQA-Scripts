from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.get('https://jaikun12.github.io/simple-task-app/?fbclid=IwAR2wnYwGMEtNvkKPj-z8C05Ae3BZa0zwbam0Evy1LXdzOxwalPXq140EsQo')


N = 20
x = '.jpeg'

for i in range(N):
    name = "task" + str(i + 1)
    tasks = driver.find_element_by_id("task-input")
    tasks.clear()
    tasks.send_keys(name)
    tasks.send_keys(Keys.RETURN)
    driver.save_screenshot(str(i + 1) + x)
    tasklist = driver.find_elements_by_tag_name('li')
    print(len(tasklist))
