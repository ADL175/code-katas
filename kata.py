
#8kyu 1pt
def find_multiples(integer, limit):
    new_list = []
    product = 0
    while product < limit:
        product += integer
        if product <= limit:
            new_list.append(product)
    return new_list

# Best solution in one line
# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))

# if __name__ == '__main__':
#     print('potato')

#7kyu 2pt
def validate_pin(pin):
    #return true or false
    if int(str(pin).isdigit()) and len(pin) == 4 or len(pin) == 6:
            return True
    else:
        return False

# Best solution
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()

#6kyu 3pt / not working
# def reverse(str):
#     str = list(str)
#     str.append('%')
#     for i in range(len(str)-1):
#         if str[i].upper() == str[i + 1].upper() or str[i].upper() == str[i - 1].upper():
#             if str[i].isupper():
#                 str[i] = str[i].lower()
#             elif str[i].islower():
#                 str[i] = str[i].upper()
#     del str[-1]
#     return ''.join(str)

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

# Best solutions
# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])


#7kyu 2pt 
def calculate_years(principal, interest, tax, desired):
    tally = 0
    while principal < desired:
        profit = (principal * interest)*(1-tax)
        principal += profit
        tally += 1
    return tally

#7kyu 2pt 
def high_and_low(numbers):
    num_str_list = list(numbers.split())
    min_max_string = ""
    for i in range(len(num_str_list)):
        num_str_list[i] = int(num_str_list[i])
    min_max_string = str(max(num_str_list)) + " " + str(min(num_str_list))
    return min_max_string

# def high_and_low(numbers):
#   n = map(int, numbers.split(' '))
#   return str(max(n)) + ' ' + str(min(n))


#6kyu 3pt 
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
#12 score

#6kyu 3pt 
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

#15 score

#7kyu 2pt 
def find_short(s):
    s = s.split()
    min_word = len(s[0])
    for i in s:
        if len(i) < min_word:
            min_word = len(i)
    return min_word

#17 score


#6kyu score
def alphabet_position(text):
    text = list(text.lower())
    num_list = ""
    for i in text:
        if ord(i) >= 97 and ord(i) <=122:
            num_list += (str(int(ord(i))-96)) + ' '
    return num_list[:-1]
#20 score