## **[DefaultDict Tutorial](https://www.hackerrank.com/challenges/defaultdict-tutorial)** 

The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

In this challenge, you will be given **2** integers, **m** and **n**. There are **n** words, which might repeat, in word group *A*. There are  words belonging to word group *B*. For each  words, **m** check whether the word has appeared in group  *A* or not. Print the indices of each occurrence of **m** in group *A*. If it does not appear, print *-1*.

For example:  
```
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
```

This prints:
```
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
```

**Sample Input 0**  
```
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
```

**Sample Output 0**  
```
1 2 4
3 5
```

**Explanation 0**  
'a' appeared `3` times in positions `1`,`2` and `4`.
'b' appeared `2` times in positions `3` and `5`.
In the sample problem, if 'c' also appeared in word group `B`, you would print `-1`.
