## [Eye and Identity](https://www.hackerrank.com/challenges/np-eye-and-identity)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        95.55% |

[**identity**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.identity.html#numpy.identity)


The **identity** tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0. The default type of elements is float.



```
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

```

[**eye**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html#numpy-eye) 


The *eye* tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter K. A positive K is for the upper diagonal, a negative K is for the lower, and a 0K  (default) is for the main diagonal.



```
import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.

```



---


**Task** 


Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.


**Note** 


In order to get alignment correct, please insert the line  *[SVG image]*  below the numpy import. 

**Input Format**

A single line containing the space separated values of M and N.
N denotes the rows.
M denotes the columns.

**Output Format**
Print the desired N X Marray.

**Sample Input**


```
3 3

```
**Sample Output**


```
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Eye and Identity](./eye_and_identity.py)

| Submissions                                                                              |                                          Leaderboard                                          |                                                                              Discussions |                                                                          Editorial |
| :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-eye-and-identity/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-eye-and-identity/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-eye-and-identity/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-eye-and-identity/editorial) |

