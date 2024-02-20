from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
driver = webdriver.Chrome() 
url =driver.get( 
    "https://www.saucedemo.com/") 
print(driver.find_element_by_xpath("Webpage_task_11").text) 
driver.close()