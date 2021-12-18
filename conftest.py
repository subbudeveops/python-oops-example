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