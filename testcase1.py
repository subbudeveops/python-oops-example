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