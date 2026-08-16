import re

# A valid email must have the format: username@websitename.extension
#   - username:    letters, digits, dashes, underscores   [A-Za-z0-9_-]
#   - websitename: letters and digits only               [A-Za-z0-9]
#   - extension:   letters only, at most 3 characters      [A-Za-z]{1,3}
def fun(s):
    pattern = r"^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$"
    return bool(re.fullmatch(pattern, s))


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input().strip())
    # Keep only the valid emails and sort them lexicographically.
    filtered_emails = filter_mail(emails)
    print(sorted(filtered_emails))
