from selenium import webdriver 
from time import sleep 
driver = webdriver.Chrome() 
def wait():
        sleep(5)
url = "https://www.saucedemo.com/"
driver.get(url) 
get_title = driver.title  
print(get_title)
