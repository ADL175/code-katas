"""Testing proper_parenthetics function."""
import pytest
from sort_cards import sort_cards

testdata = [
    (sort_cards(list('39A5T824Q7J6K')), list('A23456789TJQK')),
    (sort_cards(list('Q286JK395A47T')), list('A23456789TJQK')),
    (sort_cards(list('54TQKJ69327A8')), list('A23456789TJQK'))
]


@pytest.mark.parametrize('random_cards, result', testdata)
def test_sort_cards(random_cards, result):
    """Testing sort_cards works for all cases."""
    assert sort_cards(random_cards) == result
