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
