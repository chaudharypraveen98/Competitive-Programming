import re

# A valid credit card number must satisfy ALL of these rules:
#   - It must start with 4, 5 or 6.
#   - It must contain exactly 16 digits.
#   - It must only consist of digits (0-9), optionally grouped in blocks of 4
#     separated by a single hyphen "-".
#   - It must NOT have 4 or more consecutive repeated digits.

# Structure pattern:
#   ^[456]\d{3}        : starts with 4/5/6 followed by 3 more digits.
#   (-?\d{4}){3}$      : three more groups of 4 digits, each optionally
#                        preceded by a single "-". This enforces the
#                        "groups of 4" and the "exactly 16 digits" rules.
structure = r"^[456]\d{3}(-?\d{4}){3}$"

# Pattern used to detect 4 or more consecutive repeated digits.
# (\d)\1{3,} matches a digit followed by the same digit 3 or more times.
repeat = r"(\d)\1{3,}"

n = int(input())
for _ in range(n):
    card = input().strip()

    # First, validate the overall structure.
    if not re.fullmatch(structure, card):
        print("Invalid")
        continue

    # Remove hyphens before checking for consecutive repeated digits, so
    # that digits separated only by a hyphen are still considered consecutive.
    digits_only = card.replace("-", "")
    if re.search(repeat, digits_only):
        print("Invalid")
    else:
        print("Valid")
