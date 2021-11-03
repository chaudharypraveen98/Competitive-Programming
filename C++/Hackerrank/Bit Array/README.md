## **[Bit Array](https://www.hackerrank.com/challenges/bitset-1)** 
You are given four integers: N,S ,P , Q. You will use them in order to create the sequence **a** with the following pseudo-code.
```
a[0] = S (modulo 2^31)
for i = 1 to N-1
    a[i] = a[i-1]*P+Q (modulo 2^31) 
```
Your task is to calculate the number of distinct integers in the sequence **a**.

#### Input Format

Four space separated integers on a single line, N,S ,P , and Q respectively.

#### Output Format

A single integer that denotes the number of distinct integers in the sequence **a**.


#### Sample Input
```
3 1 1 1
```
#### Sample Output
```
3
```
#### Explanation
a = [1,2,3]
Hence, there are 3 different integers in the sequence.