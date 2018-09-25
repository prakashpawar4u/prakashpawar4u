from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


browser = webdriver.Firefox(executable_path=r"C:\Users\pawarp\Downloads\geckodriver.exe")
browser.get("http://www.facebook.com")
time.sleep(10)


username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_id("loginbutton")

username.send_keys("me")
password.send_keys("newpass")

submit.click()


wait = WebDriverWait( browser, 5)

try:
    page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)

except TimeoutException:
    self.fail("Loading timeout expired")

self.assertEqual(browser.current_url, correct_page, msg = "Successful Login")
