from MyFunctions import mySum, myDiv
import pytest

def test_basic():
    assert mySum(10, 5) == 15.0

def test_except():
    """
    This test case validates that an exception is raised when dividing by 0
    :return:
    """
    with pytest.raises(Exception) as exp:
        myDiv(10, 0)
    assert exp.type == ValueError

#----- Fixtures example (a way to initialize test functions) ---
# Fixtures are used mainly to reuse code that multiple test functions may use

# This function uses a fixture which is defined in conftest.py
# (IT MUST BE NAMED LIKE THAT) and automatically added I don't have to import it
def test_fix(myfixture):
    x, y = myfixture  # These values come from the fixture
    assert mySum(x, y) == 12

#----- Parameterization (to test more than one thing on a function)
@pytest.mark.parametrize("x,y,result",[
    (1,2,3),
    (-1, 2, 1),
    (1, -2, -1)])
def testWithParams(x,y,result):
    assert mySum(x,y) == result


