import pytest
from selenium import webdriver
import time
class  TestGoogleSearch:
    @pytest.yield_fixture()
    def setUpTearDown(self):
        global driver
        driver=webdriver.Firefox(executable_path='E:\library\geckodriver.exe')
        driver.get('http://google.com')
        #driver.get("https://google.co.in / search?q = geeksforgeeks")
        driver.maximize_window()
        yield
        time.sleep(30)
        #driver.close()
    def test_Googlesearch(self,setUpTearDown):
        driver.find_element_by_name('q').send_keys('mahesh babu')
        time.sleep(5)
        driver.find_element_by_name('btnk').click()
        time.sleep(5)
        driver.find_element_by_class_name('LC201b').click()
