## [Dot and Cross](https://www.hackerrank.com/challenges/np-dot-and-cross)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        98.65% |

[**dot**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html)


The *dot* tool returns the dot product of two arrays.



```
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11

```

[**cross**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.cross.html)


The *cross* tool returns the cross product of two arrays.



```
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2

```



---


**Task**


You are given two arrays  *[SVG image]*  and  *[SVG image]* . Both have dimensions of  *[SVG image]* X *[SVG image]* .   

Your task is to compute their [matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication#Matrix_product_.28two_matrices.29).

**Input Format**

The first line contains the integer **N**.
The next **N** lines contains **N** space separated integers of array **A**.
The following **N** lines contains **N** space separated integers of array **B**.

**Output Format**

Print the matrix multiplication of  *[SVG image]*  and  *[SVG image]* .

**Sample Input**


```
2
1 2
3 4
1 2
3 4

```
**Sample Output**


```
[[ 7 10]
 [15 22]]

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Dot and Cross](./dot_and_cross.py)

| Submissions                                                                           |                                        Leaderboard                                         |                                                                           Discussions |                                                                       Editorial |
| :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-dot-and-cross/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-dot-and-cross/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-dot-and-cross/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-dot-and-cross/editorial) |

