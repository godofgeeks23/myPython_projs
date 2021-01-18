# this will play teri mitti song in youtube
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://youtube.com')
searchbox = driver.find_element_by_name('search_query')
searchbox.send_keys('Teri Mitti')
searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()
video = driver.findElement(By.id(
    "Teri Mitti - Kesari | Akshay Kumar & Parineeti Chopra | Arko | B Praak | Manoj Muntashir"))
video.click()
