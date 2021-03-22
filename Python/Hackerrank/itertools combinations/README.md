## **[itertools.combinations()](https://www.hackerrank.com/challenges/itertools-combinations)** 
itertools.combinations(iterable, r)
This tool returns the length subsequences of elements from the input iterable.<br>Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

#### Sample Code
<code>>>> from itertools import combinations</code>
<code>>>> print list(combinations('12345',2))</code>
<code>[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]</code>
<code>>>> A = [1,1,3,3,3]</code>
<code>>>> print list(combinations(A,4))</code>
<code>[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]</code>

Task  
You are given a string ```S```.
Your task is to print all possible combinations, up to size ```k``` , of the string in lexicographic sorted order.

##### Sample Input 0 
```HACK 2```

##### Sample Output 0  
<code>A
C
H
K
AC
AH
AK
CH
CK
HK</code>