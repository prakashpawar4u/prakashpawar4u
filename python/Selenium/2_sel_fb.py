from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

user = "prakashpawar4u@gmail.com"
pwd = "paapi000888000"

#driver = webdriver.Chrome(executable_path=r"C:\Users\pawarp\Downloads\chromedriver.exe")

driver = webdriver.Firefox(executable_path=r"C:\Users\pawarp\Downloads\geckodriver.exe")
driver.get("http://www.facebook.com")
time.sleep(10)
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)

elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)

elem.send_keys(Keys.RETURN)

time.sleep(60)


driver.close()
