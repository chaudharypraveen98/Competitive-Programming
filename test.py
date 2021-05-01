for j in range(int(input())):
    input_string = input().split()
    given_pattern = list('CJJCCC')
    string_given = list(input_string[2:][0])
    for index,character in enumerate(string_given):
        if character=='?':
            string_given[index] = given_pattern[index]

    final_string = "".join(string_given)
    if final_string==given_pattern:
        result = 0
        result+=int(input_string[0])*final_string.count('CJ')
        result+=int(input_string[1])*final_string.count('JC')
        print(result)
    else:
        print(0)