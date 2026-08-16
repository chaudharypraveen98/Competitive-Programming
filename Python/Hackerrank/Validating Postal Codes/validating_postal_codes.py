import re

# regex_integer_in_range: matches a 6-digit number from 100000 to 999999.
# The first digit must be 1-9 and the remaining 5 digits can be anything 0-9.
regex_integer_in_range = r"^[1-9]\d{5}$"

# regex_alternating_repetitive_digit_pair: matches a digit that is followed
# (with exactly one other digit in between) by the same digit again. This is
# an "alternating repetitive digit pair" (e.g. in "121" the 1's form a pair).
#   (\d)        : capture a digit
#   (?=\d\1)    : look ahead for any digit followed by the same captured digit
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

P = input()
print(
    bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)
