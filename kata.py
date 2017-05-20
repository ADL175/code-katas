
"""Kata: Find Multiples of a Number by Spherixo

#1 Best Practices Solution by acaccia, gregoryltwong, BluellDragon, TehOrange, igor-gurkin, SteveAhn (plus 43 more warriors)

https://www.codewars.com/kata/58ca658cc0d6401f2700045f

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
"""

#8kyu 1pt
def find_multiples(integer, limit):
    new_list = []
    product = 0
    while product < limit:
        product += integer
        if product <= limit:
            new_list.append(product)
    return new_list

"""Kata: Regex validate PIN code by JMurphyWeb

#1 Best Practices Solution by CrazyMerlyn, pivek303, lechevalier, aytrack, bugaevc, andriis (plus 35 more warriors)

https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
"""

#7kyu 2pt
def validate_pin(pin):
    #return true or false
    if int(str(pin).isdigit()) and len(pin) == 4 or len(pin) == 6:
            return True
    else:
        return False

"""Kata: Complementary DNA

#1 Best Practices Solution by JustyFY, ChingChangChong, pompeu2004

https://www.codewars.com/kata/554e4a2f232cdd87d9000038

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
"""

#7kyu 2pt
def DNA_strand(dna):
    print(dna)
#     dna = list(dna)
#     print(dna)
    new_dna = ""
    for i in range(len(dna)):
        if dna[i] == "A":
            new_dna += "T"
        elif dna[i] == "T":
            new_dna += "A"
        elif dna[i] == "C":
            new_dna += "G"
        elif dna[i] == "G":
            new_dna += "C"
    return new_dna

"""Kata: Money, Money, Money

#1 Best Practices Solution by hchokshi, jonathan-j-lee, Cronokirby, Robbentheking, tiffanydu31, curlew77

https://www.codewars.com/kata/563f037412e5ada593000114

def calculate_years(principal, interest, tax, desired):
    years = 0

    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1

    return years
"""

#7kyu 2pt
def calculate_years(principal, interest, tax, desired):
    tally = 0
    while principal < desired:
        profit = (principal * interest)*(1-tax)
        principal += profit
        tally += 1
    return tally

"""Kata: Highest and Lowest

#1 Best Practices Solution by Deantwo, mwdbjbc

https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
"""

#7kyu 2pt
def high_and_low(numbers):
    num_str_list = list(numbers.split())
    min_max_string = ""
    for i in range(len(num_str_list)):
        num_str_list[i] = int(num_str_list[i])
    min_max_string = str(max(num_str_list)) + " " + str(min(num_str_list))
    return min_max_string

"""Kata: Find the odd int

#1 Best Practices Solution by cerealdinner, ynnake, sfr, netpsychosis, VadimPopov, anaskhan96 (plus 184 more warriors)

https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""

#6kyu 4pt
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

"""Kata: Mysterious function

#1 Best Practices Solution by Unnamed

https://www.codewars.com/kata/mysterious-function/solutions/python

def get_num(n):
    return sum({'0': 1, '6': 1, '9': 1, '8': 2}.get(d, 0) for d in str(n))
"""

#6kyu 4pt
def get_num(n):
    tally = 0
    n = list(str(n))
    print(n)
    for i in n:
        if i == '0' or i == '6' or i == '9':
            tally += 1
        elif i == '8':
            tally += 2
    print(tally)
    return tally

"""Kata: Shortest Word

#1 Best Practices Solution by MiraliN, Cptnprice, FranzSchubert92, Chris_Rands, Mr.Child, gallione11 (plus 25 more warriors)

https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(s):
    return min(len(x) for x in s.split())
"""

#7kyu 2pt 
def find_short(s):
    s = s.split()
    min_word = len(s[0])
    for i in s:
        if len(i) < min_word:
            min_word = len(i)
    return min_word

"""Kata: Replace With Alphabet Position

#1 Best Practices Solution by laoris, murpium, CrazyMerlyn, datagram, Karan@CodeDoor, thamiamrani (plus 9 more warriors)

https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""


#6kyu 4pt
def alphabet_position(text):
    text = list(text.lower())
    num_list = ""
    for i in text:
        if ord(i) >= 97 and ord(i) <= 122:
            num_list += (str(int(ord(i))-96)) + ' '
    return num_list[:-1]
