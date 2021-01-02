""""
 ------Explanation of the Answer----

1) Understanding RIGHT SHIFT >> First let's understand whats right shift by 5 (>>5) means, right shifting a number by 5 is like dividing the number by 2^5 and rounds it to the nearest lower number (floor) e.g # 64>>5 ==> 2 because 64 / 32 is 2 # 63>>5 ==> 1 # 65>>5 ==> 2
2)Understanding ord()

    ord gives the ascii values of the specified character
Ascii value of a-z ==> 97-122
               A-Z ==> 65-90
               0-9 ==> 48-57
e.g
  ord('d')  ==> 100
3) ord(c) >> 5

i)a-z ascii value when right shifted by 5 always gives 3 (97 to 122) when divided by 2^5 (i.e 32) and floored always gives 3

ii)A-Z ascii value when right shifted by 5 always gives 2 (65 to 90) when divided by 2^5 (i.e 32) and floored always gives 2

iii)0-9 ascii values when right shifted by 5 always gives 1 (48 to 57) when divided by 2^5 (i.e 32) and floored always gives 1

4) ** minus ord(c) >>5 ** 5) Since we are sorting the list in descending order i.e a-z has the highest value 3 so it needs to come first


------Alternative answers------

# Alternative answer 1
# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

# Alternative answer 2
# order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
# print(*sorted(input(), key=order.index), sep='')

# Alternative answer 3
# import string
# print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')

"""

print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')


