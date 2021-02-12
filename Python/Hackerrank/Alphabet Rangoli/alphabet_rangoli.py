import string


def print_rangoli(size):

    # It uses the string library of python
    alpha = string.ascii_lowercase
    L = []

    # it will start generation pattern from middle like c-b-a-b-c if length is 3
    for i in range(size):
        # It will join the character of strings with "-" like a-b-c
        s = "-".join(alpha[i:size])

        # It will append a row pattern like c-b-a-b-c if length is 3
        L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

    # L[:0:-1] will print the list in reverse order then by sequential order
    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    size = int(input())
    print_rangoli(size)
