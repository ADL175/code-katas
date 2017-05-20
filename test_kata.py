import pytest


# @pytest.mark.parametrize('n, lmt, result', [1, 2 [1, 2]])
def test_find_multiples():
    from kata import find_multiples
    assert find_multiples(5, 25) == [5, 10, 15, 20, 25]

# Test.expect(find_multiples(5, 25) == [5, 10, 15, 20, 25], "{0} should equal [5, 10, 15, 20, 25]".format(str(find_multiples(5, 25))))
# Test.expect(find_multiples(1, 2) == [1, 2], "{0} should equal [1, 2]".format(str(find_multiples(1, 2))))


def test_validate_pin():
    from kata import validate_pin
    assert validate_pin("00000000") == False

# def test_validate_pin(pin)
# Test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")
# Test.assert_equals(validate_pin("1111"),True, "Wrong output for '1111'")
# Test.assert_equals(validate_pin("123456"),True, "Wrong output for '123456'")

# def test_reverse():
#     from kata import reverse
#     assert reverse(5, 25) == [5, 10, 15, 20, 25]

# def test_reverse():
# test.it("Should return: 'heLLo world'")
# test.assert_equals(reverse('hello world'), 'heLLo world')
# test.it("Should return: 'HEllO WORLD'")
# test.assert_equals(reverse('HELLO WORLD'), 'HEllO WORLD')
# test.it("Should return: 'HeLlo World''")
# test.assert_equals(reverse('HeLlo World'), 'HelLo World')
# test.it("Should return: 'www'")
# test.assert_equals(reverse('WWW'), 'www')

def test_DNA_strand():
    from kata import DNA_strand
    assert DNA_strand("AAAA") == "TTTT"

# def test_DNA_strand()
# Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
# Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
# Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")


def test_calculate_years():
    from kata import calculate_years
    assert calculate_years(1000, 0.05, 0.18, 1100) == 3

# def test_calculate_years()
# Test.describe("calculate_years")
# Test.it("works for some examples")
# Test.assert_equals(calculate_years(1000, 0.05, 0.18, 1100), 3)
# Test.assert_equals(calculate_years(1000,0.01625,0.18,1200), 14)
# Test.assert_equals(calculate_years(1000,0.05,0.18,1000), 0)

def test_high_and_low():
    from kata import high_and_low
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"

# def test_high_and_low()
# Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
# Test.assert_equals(high_and_low("1 -1"), "1 -1");
# Test.assert_equals(high_and_low("1 1"), "1 1");


def test_find_it():
    from kata import find_it
    assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5

# def find_it()
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

def test_get_num():
    from kata import get_num
    assert get_num(89282350306) == 8

# def get_num()
# Test.expect(get_num(300) == 2, "Wrong output!")
# Test.expect(get_num(90783) == 4, "Wrong output!")
# Test.expect(get_num(123321) == 0, "Wrong output!")
# Test.expect(get_num(89282350306) == 8, "Wrong output!")
# Test.expect(get_num(3479283469) == 5, "Wrong output!")

def test_find_short():
    from kata import find_short
    assert find_short("bitcoin take over the world maybe who knows perhaps") == 3

# def find_short()#
# test.describe("Basic Tests")
# test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
# test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
# test.assert_equals(find_short("lets talk about javascript the best language"), 3)
# test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
# test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)

def test_alphabet_position():
    from kata import alphabet_position
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

# def test_alphabet_position():
#     from random import randint
# test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
# test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
# number_test = ""
# for item in range(10):
#     number_test += str(randint(1, 9))
# test.assert_equals(alphabet_position(number_test), "")