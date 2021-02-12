def merge_the_tools(string, k):

    # k as the third argument plays a role as a step
    for i in range(0, len(string), k):

        # generate a word of fix length
        word = string[i:i + k]
        sub_sequence = ""

        # it just loop through the word to remove duplicate
        # we haven't use set because it doesn't maintain order
        for j in word:
            if j not in sub_sequence:
                sub_sequence += j
        print(sub_sequence)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
