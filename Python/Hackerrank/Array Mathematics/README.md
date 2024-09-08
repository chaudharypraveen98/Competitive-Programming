## [Array Mathematics](https://www.hackerrank.com/challenges/np-array-mathematics)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        95.01% |

Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the *NumPy* module. 



```
import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]

```



---


**Task** 


You are given two integer arrays,  and  of dimensions X.

Your task is to perform the following operations:

1. Add (A + B)
2. Subtract (A - B)
3. Multiply (A * B)
4. Integer Division (A / B)
5. Mod (A % B)
6. Power (A ** B)


**Note**   

There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division. 

**Input Format**

The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.

**Output Format**

Print the result of each operation in the given order under **Task**.

**Sample Input**


```
1 4
1 2 3 4
5 6 7 8
```
**Sample Output**  
```
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

```

Use `//` for division in Python 3\. 


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Array Mathematics](./array_mathematics.py)

| Submissions                                                                               |                                          Leaderboard                                           |                                                                               Discussions |                                                                           Editorial |
| :---------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-array-mathematics/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-array-mathematics/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-array-mathematics/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-array-mathematics/editorial) |

