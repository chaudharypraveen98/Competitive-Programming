# collection Counter, where elements are stored as dictionary keys and their counts are stored as dictionary values.
from collections import Counter


def get_logo(logo_string):

    # It will find the most common three elements
    logo_count = Counter(logo_string).most_common(3)
    return logo_count


if __name__ == '__main__':
    s = input()
    result = get_logo(sorted(s))
    
    # *i unpacking of list
    for i in result: print(*i)
