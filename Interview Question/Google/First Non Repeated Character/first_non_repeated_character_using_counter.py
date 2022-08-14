from collections import Counter

test_str = input()

# Counter will count the number of times the number is repeated or appear
element_count = Counter(test_str)
for element in element_count:
    
    # checking if the element is repaeted once or not
    if element_count[element]==1:
        print(element)
        break
