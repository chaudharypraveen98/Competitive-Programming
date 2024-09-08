def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))


if __name__ == '__main__':
    s = input()
    print(solve(s))
