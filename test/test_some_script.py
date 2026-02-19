

import pytest
from package.some_script import TestClass

@pytest.mark.parametrize("x,y,expected_result", 
        [(1,0, 1), (0,1,1)]
    )
def test_add(x, y, expected_result):
    obj = TestClass()
    result = obj.add(x, y)
    assert  result == expected_result, f"Error: {x} + {y} returned unexpected result: {result}"


def test_build(build):
    assert build == True, "Build Package failed"

def test_install(install):
    assert install == True, "Installation failed"
