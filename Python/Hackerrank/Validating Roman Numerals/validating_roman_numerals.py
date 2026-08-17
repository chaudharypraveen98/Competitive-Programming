import re

# A valid Roman numeral uses the symbols M, D, C, L, X, V, I and represents
# a number between 1 and 3999. To validate it with a single regex we build
# the number out of four parts: thousands, hundreds, tens and units. Each
# part allows the subtractive notation (e.g. IV=4, IX=9, XL=40, XC=90,
# CD=400, CM=900).

# Thousands: M{0,3}            -> 0 to 3 thousands (range 0..3999)
# Hundreds:  (CM|CD|D?C{0,3})
# Tens:      (XC|XL|L?X{0,3})
# Units:     (IX|IV|V?I{0,3})
thousand = r"M{0,3}"
hundred = r"(CM|CD|D?C{0,3})"
ten = r"(XC|XL|L?X{0,3})"
unit = r"(IX|IV|V?I{0,3})"
regex = r"^" + thousand + hundred + ten + unit + "$"

s = input()
print(bool(re.match(regex, s)))
