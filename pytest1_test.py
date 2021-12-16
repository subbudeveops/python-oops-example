import pytest
@pytest.yield_fixture()
def setUptearDown():
    print('setUp activity')
    yield
    print('tearDown activity')
@pytest.yield_fixture(scope='module')
def setUptearDownClass():
    print('setUpClass activity')
    yield
    print('tearDownClass activity')
def test_methodA(setUptearDown,setUptearDownClass):
    print('test_method A execution.....')
def test_methodB(setUptearDown,setUptearDownClass):
    print('test_method B execution.....')