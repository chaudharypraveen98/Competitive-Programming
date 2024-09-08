## [Shape and Reshape](https://www.hackerrank.com/challenges/np-shape-reshape)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        95.32% |

[**shape**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html#numpy-ndarray-shape)


The *shape* tool gives a tuple of array dimensions and can be used to change the dimensions of an array.


**(a). Using *shape* to get array dimensions**



```
import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 1 row and 5 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 

```

**(b). Using *shape* to change array dimensions** 



```
import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
[[1 2]
[3 4]
[5 6]]

```

[**reshape**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html#numpy.reshape)


The *reshape* tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself. 



```
import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]

```



---


**Task** 


You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

**Input Format**

A single line of input containing  *[SVG image]*  space separated integers.

**Output Format**

Print the  *[SVG image]* X *[SVG image]*  *NumPy* array.

**Sample Input**


```
1 2 3 4 5 6 7 8 9

```
**Sample Output**


```
[[1 2 3]
 [4 5 6]
 [7 8 9]]

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Shape and Reshape](./shape_and_reshape.py)

| Submissions                                                                           |                                        Leaderboard                                         |                                                                           Discussions |                                                                       Editorial |
| :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-shape-reshape/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-shape-reshape/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-shape-reshape/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-shape-reshape/editorial) |

