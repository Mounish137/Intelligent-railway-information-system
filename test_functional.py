from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_fields():
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')
    src_box = browser.find_element_by_name('src')
    dest_box = browser.find_element_by_name('dest')
    src_box.send_keys('MUGR')
    dest_box.send_keys('SC')
    browser.find_element_by_id('submit_button').click()
    time.sleep(10)
    browser.quit()
