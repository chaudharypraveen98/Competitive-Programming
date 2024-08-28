Link -> [Permutations of a given string](https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1)

## Approach
- Observe the pattern, we need to select one character each item, and create string
- We need to also check duplicates
- Used set for performance because of checking item in set is O(1), you can use array itself and avoid last conversion to list
- We iterate the options available, select that item and filter that item from list and continue this `options[0:i]+options[i+1:]` 
- Write the Base condition
- Hurray! Done