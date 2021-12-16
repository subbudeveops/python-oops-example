import unittest
class TestCase2(unittest.TestCase):
    def setUp(self):
        print('TestCaase2:setUp')
    def test1(self):
        print('TestCase2:Test1')
   
    def tearDown(self):
        print('TestCase2:TearDown')