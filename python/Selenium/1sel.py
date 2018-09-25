from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path=r"C:\Users\pawarp\Downloads\chromedriver.exe")

driver = webdriver.Firefox(executable_path=r"C:\Users\pawarp\Downloads\geckodriver.exe")
driver.get("http://www.python.org")
