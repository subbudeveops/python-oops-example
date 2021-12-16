import unittest
from testcase1 import *
from testcase2 import *
#we have to load all test from testcase1
tc1=unittest.TestLoader().loadTestsFromTestCase(TestCase1)
#we have to load all test from testcase2
tc2=unittest.TestLoader().loadTestsFromTestCase(TestCase2)
ts=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(ts)