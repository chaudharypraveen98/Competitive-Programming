## **[Set .add()](https://www.hackerrank.com/challenges/py-set-add)** 
If we want to add a single element to an existing set, we can use the <em>.add()</em> operation. <br>
It adds the element to the set and returns '<strong><code>None</code></strong>'.

##### Example  
```
>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
```

###### Task  
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of country stamps.

Find the total number of distinct country stamps.

**Sample Input 0**  
```
7
UK
China
USA
France
New Zealand
UK
France
```

**Sample Output 0**  
`5`

**Explanation 0**  
UK and France repeat twice. Hence, the total number of distinct country stamps is `5`(five).