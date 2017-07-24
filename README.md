string_pyramid:

Worked intermittently with Miguel Pena during this kata. This pyramid is built from characters from a given string.

The first method -watch_pyramid_from_the_side(characters): shows the pyramid as you would see from the side.
The second method -watch_pyramid_from_above(characters): shows the pyramid as you would see from above.
The third method -count_visible_characters_of_the_pyramid(characters):  returns the count of all characters, that are visible from outside the pyramid.
The forth method -count_all_characters_of_the_pyramid(characters): should count all characters of the pyramid. The pyramid is completely solid and has no holes or rooms in it.

Every character will be used for building one layer of the pyramid. So the length of the given string will be the height of the pyramid. Every layer will be built with stones from the given character. There is no limit of stones.
The pyramid should have perfect angles of 45 degrees.

Example: Given string: "abc"
Pyramid from the side: returns

  c
 bbb
aaaaa

Pyramid from above: returns

aaaaa
abbba
abcba
abbba
aaaaa

Count of visible stones/characters:
returns 25
Count of all used stones/characters:
returns 35
<!-- Code Kata from ^^^from http://www.codewars.com/kata/string-pyramid -->

...
sort_cards README:

The sort_cards() function sorts a shuffled list of cards, so that any given list of cards is sorted by rank, no matter the starting collection.

All cards in the list are represented as strings, so that sorted list of cards looks like this:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:

sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

<!-- ^^^*From https://www.codewars.com/kata/sort-deck-of-cards/python -->

stackoverflow information on using "sorted" and ".get" on dictionary values.
<!-- ^^https://stackoverflow.com/questions/16772071/sort-dict-by-value-python -->
...
proper_parenthetics README:

Python function takes a unicode string (text) as input and returns one of three possible values:

Return 1 if the string is “open” (there are open parens that are not closed)
Return 0 if the string is “balanced” (there are an equal number of open and closed parentheses in the string)
Return -1 if the string is “broken” (a closing parens has not been proceeded by one that opens)

'(()' is open: 1
'((()))' is balanced: 0
'()))' is broken: -1
...



# code-katas
Day 5 code wars challenges
# Completed Katas
#8kyu x 1
#7kyu x 6
#6kyu x 2
**Opposite Number (8th kyu)**
Kata: Find Multiples of a Number by Spherixo
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/58ca658cc0d6401f2700045f

...


**Opposite Number (7th kyu)**
Kata: Regex validate PIN code by JMurphyWeb
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

...

**Opposite Number (7th kyu)**
Kata: Complementary DNA
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/554e4a2f232cdd87d9000038


...

**Opposite Number (7th kyu)**
Kata: Money, Money, Money
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/563f037412e5ada593000114

...

**Opposite Number (7th kyu)**
Kata: Highest and Lowest
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/554b4ac871d6813a03000035


...

**Opposite Number (6th kyu)**
Kata: Find the odd int
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/mysterious-function/solutions/python



...
**Opposite Number (7th kyu)**
Kata: Mysterious function
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/554b4ac871d6813a03000035


...

**Opposite Number (7th kyu)**
Kata: Shortest Word
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9


...

**Opposite Number (6th kyu)**
Kata: Replace With Alphabet Position
- **Module**: `kata.py`
- **Tests**: `test_kata.py`
- **URL**: [challenge url]https://www.codewars.com/kata/546f922b54af40e1e90001da


...
