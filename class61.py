# PYTHON UNIT TESTING:
#---------------------
# Two types of testing
#1.Unit Testing
#2.Integration Testing

#1.unit Testing:
#The process of testing wheter aparticular units is working properly or not  is called unit testing(developer  jobs only testing)

#2.Integration testing:
# The process of testing  wheter total application(end to end),it is called integration testing(QA Team job only)


#as per testing some techniqal word
#1.Test Scenario
#2.Test case
#3.Test suite

#Testing login functionality----->it is called test scenario
#--------------------------------
#valid user name and valid password-------Test case1
#valid user name and notvalid password-------Test case2
#invalid user name and valid password-------Test case3
#invalid user name and invalid password-------Test case4

#all test case to gether excuting it is called Test suite


#how to  perform unittesting in python:
#--------------------------------------
# we need unittest module we are not required to install python inbuild module  
# her this module contain one class to write test class what is that class name 'Testcase'
# This TestCase class  contain three instance methos we have to overwrite this instace method means that i have to write my own class 'TestCaseDemo'

# class TestCaseDemo(TestCase):
#     1.setup()
#     2.test()                 3 methods
#     3.teardown()


# our own class(TestcaseDemo) should be child of TestCase
#in this which methods implemented only 3 methods

#     1.setup()
#     2.test()
#     3.teardown()

import unittest
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setup method exctution')
    def test(self):
        print('test method excuting')   # Test method not fixced u can take any name but should be prefixed Test
    def tearDown(self):
        print('TearDown method executing')
unittest.main()


import unittest
from unittest.case import TestCase
class Demo(unittest.TestCase):
    def setUp(self):
        print('set up is completed')
    def test_method1(self):
        print('this is test method1 executing')
    def test_method2(self):
        print('this is test method2 executing')
        
    def tearDown(self):
        print('testDown is completed')
unittest.main()

#output:
#set up is completed
#this is test method1 executing
#testdown is completed
#.set up is completed
#this is test method2 executing
#testdown is completed
#.
#----------------------------------------------------------------------
#Ran 2 tests in 0.001s

#OK

print()
#Note: Every test method execution before that setup method is executed

#SetUpClass(cls):
#-----------
#normal setUP()methos excuting every test() method
#SetUpClass(cls) method it is class level ,for all test () method setupclass(cls) method will be excuted only once

#tearDownclass(cls):
#------------------
# only once for executing tearDownclass(cls) for all test() methods

# ex:10 test method is there how many time excuting with methods
#setUp()--->10 item excuting
#tearDown()---10 item excuting
#setupClass(cls):---->1 item excuting
#tearDownClass(cls)----> 1 item excuting

import unittest
class TestCaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass method excuting')

    def setUp(self):
        print('set up is completed')
    def test_method1(self):
        print('this is test method1 executing')
    def test_method2(self):
        print('this is test method2 executing')
        
    def tearDown(self):
        print('testDown is completed')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method executing')
unittest.main()

#output:
#setUpClass method excuting
#set up is completed
#this is test method1 executing
#testDown is completed
#.set up is completed
#this is test method2 executing
#testDown is completed
#.tearDownClass method executing

#-------------------------------------------!#---------------------------
#Ran 2 tests in 0.002s

#OK

# WHICH TEST IS EXecuting first 
# always alphabit wise executing
import unittest
class TestCaseClass(unittest.TestCase):
    def test_A(self):
        print('this is test A method executing')
    def test_C(self):
        print('this is test C method executing')
    def test_B(self):
        print('this is test  B method executing')
        
unittest.main()

#output
#this is test A method executing
#.this is test  B method executing
#.this is test C method executing
#.
#----------------------------------------------------------------------
#Ran 3 tests in 0.001s

#OK

#LIMITATION OF UNIT TESTING:
#--------------------------
#1.Test result will be display to the console only and it is not posiible to generate reports

#2.Unit test framework always executes test method alphabetical orde only and it is not possible to  customizw order

#3.AS the part of batch exceution(TestSuite),all test methods from the specified Testcase classes will be excuted and it is not possible to specify particular methos.

#4.In unittesting only limited setup and tearDown methods are available.

#setupClass()---->Before executing all test methods of a TestCase class
#teraDownClass()---->After execting all test methods of a TestCase class
#setUP()---->Before every test method Execution
#tearDown()--->After every test method execution


# TestSuite: A group of TestCase by Default consider as TestSuite
# Before satrting TestSuite i Want certane Activites     
# After completing TestSuite  i want to do sertan activites
# If we want to perform any activity before executing testsuite and after
#executing testsuite ,unittest framework does not define any methods

#TestSuite():A group od TestCase,which is called Testsuite:
#Ex:testcase1.py
import unittest
class TestCase1(unittest.TestCase):
    def setUp(self):
        print('TestCaase1:setUp')
    def test1(self):
        print('TestCase1:Test1')
    def test2(self):
        print('TestCase2:Test2')
    def tearDown(self):
        print('TestCase1:TearDown')

#Ex:testcase2.py
import unittest
class TestCase2(unittest.TestCase):
    def setUp(self):
        print('TestCaase2:setUp')
    def test1(self):
        print('TestCase2:Test1')
   
    def tearDown(self):
        print('TestCase2:TearDown')

#EX:teardown.py
import unittest
from testcase1 import *
from testcase2 import *
#we have to load all test from testcase1
tc1=unittest.TestLoader().loadTestsFromTestCase(TestCase1)
#we have to load all test from testcase2
tc2=unittest.TestLoader().loadTestsFromTestCase(TestCase2)
ts=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)




#python unittesting with selenium:
#--------------------------------
#write apython script to test Google search functionality by using selenium Unitttesing

#Selenium:package
#webdriver:module
#pip install selenium

#webdriver module contain several classes and function to test functionality of the web application
# if u want form testing we want lanuch browser
#Launch Browser:
#---------------
#Browser Driver must be required which is responisable to lanuch our browser
#download the geckodriver and create library folder

#Browser Interaction and navigation of web pages:
#------------------------------------------------
#1.driver.get(url)
# to open specified url
# iwant open facebook
#2.driver.maximize_window()
#3.driver.title()
#4.driver.current_url()
#5.driver.refresh()
#6.driver.back()--->Goes one step backward in the browser history
#7.driver.forward---->goes one step forward in the browser history
#8.driver.close()--->To close current window
#9.drive.quit()

from selenium import webdriver
driver=webdriver. Firefox(executable_path='E:\library\geckodriver')
driver.get('http://www.facebook.com/')
print('title:',driver.title)
print('current page url:',driver.current_url)
driver.get('http://durgasoftvideos.com/')
print('title:',driver.title)
print('current page url:',driver.current_url)
driver.back()  #after back current url is facebbok url
print('After Back current url:',driver.current_url)
driver.forward()
print('after Forword current url:',driver.current_url)
driver.close()

#how to interact with web elements:
#----------------------------------
# if i know the id how to get element
#driver.find_element_by_id('id')
#driver.find_element_by_name('name')
#driver.find_element_by_xpath('xpath')
#driver.find_element_by_css_selector('css')
#driver.find_element_by_link_text('text')


#driver.find_element(By.ID,'id')
#driver.find_element(By.NAME,'name')
#driver.find_element(By.LINK_TEXT,'txt')
#driver.find_element(By.CSS_SELECOT,'css')
rom selenium import webdriver
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





# To overcome all limitacation  we can go for

#pyTest Framework:
#-----------------
#1.It is advanced version of unittest framework
#2.built on top of unittest framework
#pip install pytest

#PyTest Nameing Convercation :

#1.File name should start or ends with 'test'
#ex: test_google_search.py
#    google_search_test.py

#2.Class name should start with 'Test'
# ex:TestGoogleSearch
#    TestCaseDemo

#3.test method name should starts with 'test_'
#ex: test_method1()
#    test_method2()

#Note1: File name Should start and end with test,
#Note2:class name should start with test
#Note3:Method name should be start with 'test_'
#Note4:my own file   and my own method is should not be  excuted

#ex:pytest_test.py

import pytest
def test_methodA():
    print('test_methodA execution')
def test_methodB():
    print('test_methodB execution')

#how to execute the progrma
# py.test
#output:
#============================================================= test session starts ==============================================================
#platform win32 -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
#rootdir: E:\oops
#collected 2 #items                                                                                                                               

#pytest_script_test.py .#.                                                                                                                  [100%]

#============================================================== 2 passed in 0.14s ===============================================================


#Note1: File name Should start and end with test,
#Note2:class name should start with test
#Note3:Method name should be start with 'test_'
#Note4:my own file   and my own method is should not be  excuted

import pytest
def test_methodA():
    print('test_methodA execution')
def test_methodB():
    print('test_methodB execution')
def my_testmethod1():
    print('my_testmethod execution')   # it should not executed 
#how to execute the progrma
# py.test
#output:
#============================================================= test session starts ==============================================================
#platform win32 -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
#rootdir: E:\oops
#collected 2 #items                                                                                                                               

#pytest_script_test.py .#.                                                                                                                  [100%]

#============================================================== 2 passed in 0.14s ===============================================================

#file1 is: pytest_demo1_test.py
import pytest
def test_methodA():
    print('demo1:test_methodA execution')
def test_methodB():
    print('deno1:test_methodB execution')


#file2 is:pytest_demo2_test.py
import pytest
def test_methodA():
    print("demo2:test_methodA Execution")
def test_methodB():
    print('demo2:test_methodB Execution')


#How to run two file at atime 
#py.test ---->it is executing two test script at atime
#how execute particular test script----->py.test pytest_demo1_test.py
#                                        py.test pytest_demo2_test.py

#note: by default py.test won't display print statement output  to the console
# if want that -s opition is required
# py.test -s pytest_demo1_test.py


#output:
#py.test -s pytest_demo1_test.py
#=================================================================== test session starts ====================================================================
#platform win32 -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
#rootdir: E:\oops
#collected 2 #items                                                                                                                                           

#pytest_demo1_test.py demo1:test_methodA execution
#.deno1:test_methodB execution
#.

#==================================================================== 2 passed in 0.03s =====================================================================




#output:

#py.test -s -v  pytest_demo1_test.py
#=================================================================== test session starts #====================================================================
#platform win32 -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- c:\users\user\appdata\local\programs\python\python38-32\python.exe
#cachedir: .pytest_cache
#rootdir: E:\oops
#collected 2 #items                                                                                                                                           

#pytest_demo1_test.py::test_methodA demo1:test_methodA execution
#PASSED
#pytest_demo1_test.py::test_methodB deno1:test_methodB execution
#PASSED

#==================================================================== 2 passed in 0.03s =====================================================================

#how to implement setUp()method in pytest:
#----------------------------------------
# setUp(),teraDown(),setUpclass(cls)and tearDownclass(cls) such type method not available in pytest
#By using some decorator
#  @pytest.fixture()
# we can any type of method u can use

#pytest1_test.py
import pytest
@pytest.fixture()
def setUp():
    print('setUp is executed')
def test_methodA(setUp):
    print('Executing test_methodA')
def test_methodB(setUp):
    print('Executing test_methodB')


#py.test -s -v pytest1.test.py



# how to implement tearDown() in pytest:
#--------------------------------------
# @pytest.fixture()====>used  for SetUp()method
# @pytest.yield_fixture()===>>used for both setUp() and TearDown()
#  )
# def m1():  ===> this method meant for both activite
#   setUp activite
#   yield
#   tearDown activite


# pytest1_test.py
import pytest
@pytest.yield_fixture()
def setUptearDown():
    print('setUp activity')
    yield
    print('tearDown activity')
def test_methodA(setUptearDown):
    print('test_methodoA is executed')
def test_methodB(setUptearDown):
    print('test_methodB is executed')

#py.test -s -v pytest1.test.py



#how to implement setUpclass() and tearDownclass() in pytest:
#-------------------------------------------------------------
# @pytest.yield_fixture(scope='module')

# pytest1_test.py
import pytest
@pytest.yield_fixture(scope='module')
def setUptearDownclass():
    print('setUpClass activity')
    yield
    print('tearDownClass activity')
def test_methodA(setUptearDownclass):
    print('test_methodA is executed')
def test_methodB(setUptearDownclass):
    print('test_methodB is executed')

#py.test -s -v pytest1.test.py


#how to implement setUp(),tearDown() and setUpClass(),tearDownClass() functionalty simultaneously inpytest:
#---------------------------------------------------------------------------------------------------------
# pytest1_test.py
import pytest
@pytest.yield_fixture()
def setUptearDown():
    print('setUp activity')
    yield
    print('tearDown acitvity')
@pytest.yield_fixture(scope='module')
def setUptearDownClass():
    print('setUpClass activity')
    yield
    print('tearDownClass activity')
def test_methodA(setUptearDown,setUptearDownClass):
    print('test_method A execution.....')
def test_methodB(setUptearDown,setUptearDownClass):
    print('test_method B execution.....')

#py.test -s -v pytest1.test.py



#Note: multiple testscript required same setUp and tearDown functinality
#dont write setup and tearDown  functionality  every test script seperately uncessary length  and uncesarry duplicate of code  how to slove this problem
# we have one special file "conftest.py" this name always fixed
#common setup and tearDown code in this file.

# pytest1_test.py
def test_methodA(setUptearDown,setUptearDownClass):
    print('test1:test_method A execution.....')
def test_methodB(setUptearDown,setUptearDownClass):
    print('test1:test_method B execution.....')

#pytest2_test.py
def test_methodA(setUptearDown,setUptearDownClass):
    print('test2:test_method A execution.....')
def test_methodB(setUptearDown,setUptearDownClass):
    print('test2:test_method B execution.....')


#conftest.py   name is always fix
#code reusability
#common setup and tearDown activites, we have to define in this file automatically available for all test scripts

#conftest.py

import pytest
@pytest.yield_fixture()
def setUptearDown():
    print('setup activity')
    yield
    print('tearDown activity')
@pytest.yield_fixture(scope='module')
def setUptearDownClass():
    print('setupclass activity')
    yield
    print('tearDownClass activity')

#py.test -s -v pytest1_test.py pytest2_test.py

#Various possible ways to run pytest test scripts:
#------------------------------------------------
#1.py.test -v -s
#   To run all test methods present in all test scripts of current working dirctory

# how to run particular testscript
#2.py.test -v -s pytest1_test.py
# To run all test methods of aparticular test script

#3.how to run multiple testscript
#py.test -v -s pytest1_test.py pytest2_test.py
#  To run multiple test script

#4.i want to run perticular test_method
#py.test -v -s pytest1_test.py::test_methodA
#  To run perticular test _method

# multiple test method is there which method executing first in pytest
# pytest by default executing all method from top to bottom.
#test1.py
def test_methodC():
    print('test_methodC execution')
def test_methodA():
    print('test_methodA execution')
def test_methodB():
    print('test_methodB execution')

#Note: in pytest method is executing from top to bottom

#output
#test1.py::test_methodC test_methodC execution
#PASSED
#test1.py::test_methodA test_methodA execution
#PASSED
#test1.py::test_methodB test_methodB execution
#PASSED

#how to customize order of tests in pytest:
#------------------------------------------
# we need to install pytest-ordering module
#pip install pytest_ordering

#test1.py
import pytest
@pytest.mark.run(order=3)
def test_methodC():
    print('test_methodC execution')
@pytest.mark.run(order=1)
def test_methodA():
    print('test_methodA execution')
@pytest.mark.run(order=2)
def test_methodB():
    print('test_methodB execution')

#output
#test1.py::test_methodA test_methodC execution
#PASSED
#test1.py::test_methodB test_methodA execution
#PASSED
#test1.py::test_methodC test_methodB execution
#PASSED

#How to generate test report in html form in pytest:
#---------------------------------------------------
# we have to uinstall pytest-html module
#pip install pytest-html
#pytest -v -s test1.py --html=result1.py























