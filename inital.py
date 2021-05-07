import time 
import random
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
##
import random
import string


options = webdriver.ChromeOptions()


#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-dev-shm-usage")
options.add_argument("--user-data-dir=C:/Users/arcaz/AppData/Local/Google/Chrome/User Data/")
time.sleep(1)
driver = webdriver.Chrome(options=options)

print("wow")

time.sleep(5)


driver.get("https://www.amazon.com/gp/cart/view.html/ref=lh_cart")