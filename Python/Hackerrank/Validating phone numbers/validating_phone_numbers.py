import re

# A valid mobile number is exactly 10 digits long and starts with 7, 8 or 9.
pattern = r"^[789]\d{9}$"

n = int(input())
for _ in range(n):
    number = input().strip()
    # re.fullmatch ensures the WHOLE string matches the pattern.
    if re.fullmatch(pattern, number):
        print("YES")
    else:
        print("NO")
