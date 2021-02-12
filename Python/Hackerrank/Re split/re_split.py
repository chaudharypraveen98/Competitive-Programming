import re

# just add , and . in the pattern to find that
regex_pattern = r"[,.]"  # Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input())))
