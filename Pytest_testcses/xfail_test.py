import pytest
@pytest.mark.xfail
@pytest.mark.custom1
def test_function():
    assert 1 == 0


def idfn(val1):
    return f"Test case number{val1} and port is"

@pytest.mark.custom2
@pytest.mark.parametrize("test_id, port", [(1,1), (2,2)], ids=idfn)
def test_function_1(test_id, port):
    print(port)
    assert 1 == 1

@pytest.mark.skip("This testcase is skipped")
def test_function():
    assert 1 == 0


def abc():
    print("ABC in xfail")