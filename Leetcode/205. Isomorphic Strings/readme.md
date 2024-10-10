Link -> [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)

## Approach
1. First compare length, if unequal return False
2. create two dict for s to t and t to s mapping
3. Store the relations if not found
4. if found and incorrect/ multiple relation return False
5. return True if all works
6. Hurray ! Done.