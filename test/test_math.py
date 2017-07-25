"""
Testing for the math.py module.
"""

import friendly_computing_machine as fcm
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.add(2, 5) == 7
    assert fcm.math.add(1, 2) == 3

testdata = [
    (2, 5, 10),
    (1, 2, 2),
    (11, 9, 99,)
    (0, 0, 0)
]
@pytest.mark.parameterize("a,b,expected", testdata)
def test_mult(a,b,expected):
    assert fcm.mult(1, 2) == 2
  


