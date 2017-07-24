import pytest

"""Kata: Find Multiples of a Number by Spherixo"""

def test_find_multiples():
    from kata import find_multiples
    assert find_multiples(5, 25) == [5, 10, 15, 20, 25]

def test_find_multiples():
    from kata import find_multiples
    assert find_multiples(1, 2) == [1, 2]

def test_find_multiples():
    from kata import find_multiples
    assert find_multiples(2, 6) == [2, 4, 6]

def test_find_multiples():
    from kata import find_multiples
    assert find_multiples(3, 12) == [3, 6, 9, 12]

def test_find_multiples():
    from kata import find_multiples
    assert find_multiples(5, 29) == [5, 10, 15, 20, 25]        


"""Kata: Regex validate PIN code by JMurphyWeb"""


def test_validate_pin():
    from kata import validate_pin
    assert validate_pin("00000000") == False

def test_validate_pin():
    from kata import validate_pin
    assert validate_pin("1111") == True

def test_validate_pin():
    from kata import validate_pin
    assert validate_pin("123456") == True

def test_validate_pin():
    from kata import validate_pin
    assert validate_pin("123!") == False

def test_validate_pin():
    from kata import validate_pin
    assert validate_pin("%%^*&*") == False    


"""Kata: Complementary DNA"""



def test_DNA_strand():
    from kata import DNA_strand
    assert DNA_strand("AAAA") == "TTTT"

def test_DNA_strand():
    from kata import DNA_strand
    assert DNA_strand("TTTT") == "AAAA"

def test_DNA_strand():
    from kata import DNA_strand
    assert DNA_strand("ATTGC") == "TAACG"

def test_DNA_strand():
    from kata import DNA_strand
    assert DNA_strand("TAACG") == "ATTGC"

def test_DNA_strand():
    from kata import DNA_strand
    assert DNA_strand("GTAT") == "CATA"


"""Kata: Money, Money, Money"""


def test_calculate_years():
    from kata import calculate_years
    assert calculate_years(1000, 0.05, 0.18, 1100) == 3

def test_calculate_years():
    from kata import calculate_years
    assert calculate_years(1000,0.01625,0.18,1200) == 14

def test_calculate_years():
    from kata import calculate_years
    assert calculate_years(1000,0.05,0.18,1000) == 0

def test_calculate_years():
    from kata import calculate_years
    assert calculate_years(1000,0.01625,0.18,1000) == 0

def test_calculate_years():
    from kata import calculate_years
    assert calculate_years(1000,0.01, 0.70, 12000) == 830    

"""Kata: Highest and Lowest"""

def test_high_and_low():
    from kata import high_and_low
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"

def test_high_and_low():
    from kata import high_and_low
    assert high_and_low("1 2 4 5 66 7 2 0") == "66 0"

def test_high_and_low():
    from kata import high_and_low
    assert high_and_low("4 5 29 54 4 0 -64 1 -3 6 -6") == "54 -64"

def test_high_and_low():
    from kata import high_and_low
    assert high_and_low("1 10") == "10 1"

def test_high_and_low():
    from kata import high_and_low
    assert high_and_low("-100 300 900") == "900 300"

"""Kata: Find the odd int"""

def test_find_it():
    from kata import find_it
    assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5

def test_find_it():
    from kata import find_it
    assert find_it([23,23,656,77,88,33,66,88,22,90,88,90,90]) == 656

def test_find_it():
    from kata import find_it
    assert find_it([23,23,656,77,8,9,9,9,9]) == 656

def test_find_it():
    from kata import find_it
    assert find_it([2,2,2,25,3342349]) == 2

def test_find_it():
    from kata import find_it
    assert find_it([2,2,2,25,5,5,5,5,5,59]) == 2

"""Kata: Mysterious function"""

def test_get_num():
    from kata import get_num
    assert get_num(89282350306) == 8

def test_get_num():
    from kata import get_num
    assert get_num(8888) == 8

def test_get_num():
    from kata import get_num
    assert get_num(90783) == 4

def test_get_num():
    from kata import get_num
    assert get_num(123321) == 0

def test_get_num():
    from kata import get_num
    assert get_num(3479283469) == 5

"""Kata: Shortest Word"""

def test_find_short():
    from kata import find_short
    assert find_short("bitcoin take over the world maybe who knows perhaps") == 3

def test_find_short():
    from kata import find_short
    assert find_short("bitcoin take a over the world maybe who knows perhaps") == 1

def test_find_short():
    from kata import find_short
    assert find_short("bitcoin sksksksksksks take over the world maybe who knows perhaps") == 3

def test_find_short():
    from kata import find_short
    assert find_short("bitcoin take over the world maybe who a s a s") == 1

def test_find_short():
    from kata import find_short
    assert find_short("bitcoin 234 take over the world maybe who 234 knows perhaps") == 3            

"""Kata: Replace With Alphabet Position"""

def test_alphabet_position():
    from kata import alphabet_position
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def test_alphabet_position():
    from kata import alphabet_position
    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"

def test_alphabet_position():
    from kata import alphabet_position
    assert alphabet_position("a The sunset sets at twelve o' clock.") == "1 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def test_alphabet_position():
    from kata import alphabet_position
    assert alphabet_position("The sunset sets at twelve o' clock z.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11 26" 

def test_alphabet_position():
    from kata import alphabet_position
    assert alphabet_position("a The sunset sets at twelve o' clock. a") == "1 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11 1"    

