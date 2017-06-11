"""Testing proper_parenthetics function."""
import pytest
from proper_parenthetics import proper_parenthetics

testdata = [
    (('((())'), 1),
    (('((()))'), 0),
    (('((())))))'), -1)
]


@pytest.mark.parametrize('str, result', testdata)
def test_proper_parenthetics(str, result):
    """Testing proper_parenthetics works for all cases."""
    assert proper_parenthetics(str) == result
