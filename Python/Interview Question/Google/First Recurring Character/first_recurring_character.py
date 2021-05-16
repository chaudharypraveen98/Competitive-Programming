def first_recurring_char(word):
    # initialize the dict
    count = {}
    for char in word:

        # checking if char is already present
        if char in count:
            # if yes then returning that
            return char
        # else storing for further use
        count[char] = 1
    return None


if __name__ == '__main__':
    sample_word = input()
    print(first_recurring_char(sample_word))
