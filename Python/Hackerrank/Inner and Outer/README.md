## [Inner and Outer](https://www.hackerrank.com/challenges/np-inner-and-outer)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        98.21% |

[**inner**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.inner.html) 


The *inner* tool returns the [inner product](https://en.wikipedia.org/wiki/Inner_product_space) of two arrays.



```
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4

```

[**outer**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.outer.html) 


The *outer* tool returns the [outer product](https://en.wikipedia.org/wiki/Outer_product) of two arrays.



```
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]

```



---


**Task** 


You are given two arrays:  *[SVG image]*  and  *[SVG image]* .   

Your task is to compute their *inner* and *outer* product.

**Input Format**

The first line contains the space separated elements of array **A**.
The second line contains the space separated elements of array **B**.

**Output Format**

First, print the inner product.   

Second, print the outer product.

**Sample Input**


```
0 1
2 3

```
**Sample Output**


```
3
[[0 0]
 [2 3]]

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Inner and Outer](./inner_and_outer.py)

| Submissions                                                                             |                                         Leaderboard                                          |                                                                             Discussions |                                                                         Editorial |
| :-------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-inner-and-outer/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-inner-and-outer/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-inner-and-outer/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-inner-and-outer/editorial) |

