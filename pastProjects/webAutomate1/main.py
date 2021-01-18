# this opens youtube in the chrome browser, types in search box and click on search button!
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://youtube.com')
searchbox = driver.find_element_by_name('search_query')
searchbox.send_keys('sentdex')
searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()
time.sleep(10)
driver.quit()
