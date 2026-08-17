import re

# A valid UID must satisfy ALL of these rules:
#   1. Exactly 10 characters in length.
#   2. Only alphanumeric characters (A-Z, a-z, 0-9).
#   3. At least 2 uppercase English letters.
#   4. At least 3 digits.
#   5. No character repeats (all characters must be distinct).

# The pattern below is built from several lookaheads:
#   - (?!.*(.).*\1)              : negative lookahead that fails if any
#                                 character is repeated anywhere later.
#   - (?=(?:[a-z\d]*[A-Z]){2,}) : ensures at least 2 uppercase letters.
#   - (?=(?:\D*\d){3,})         : ensures at least 3 digits.
#   - [A-Za-z0-9]{10}           : exactly 10 alphanumeric characters.
pattern = r"^(?!.*(.).*\1)(?=(?:[a-z\d]*[A-Z]){2,})(?=(?:\D*\d){3,})[A-Za-z0-9]{10}$"

t = int(input())
for _ in range(t):
    uid = input()
    # re.fullmatch ensures the WHOLE string matches the pattern.
    if re.fullmatch(pattern, uid):
        print("Valid")
    else:
        print("Invalid")
