
from selenium import webdriver
import unittest

class GoogleSearchDemo(unittest.TestCase):
    def setUp(self):
        global driver
        driver=webdriver.Firefox(executable_path='E:\library\geckodriver')
        driver.get('http://google.com')
        driver.maximize_window()
    def test(self):
        driver.find_element_by_name(self,"q").send_keys('mahesh babu')
        time.sleep(5)
        driver.find_element_by_name('btnk').click()
        time.sleep(5)
        driver.find_element_by_name('LC201b').click
    def tearDown(self):
        print('treaDown completed')
unittest.main()
driver.close()
