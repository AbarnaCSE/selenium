from selenium import webdriver  
from time import sleep 
driver = webdriver.Chrome() 
def wait():
        sleep(5)
url = "https://www.saucedemo.com/" 
driver.get(url) 
get_url = driver.current_url  
print(get_url) 