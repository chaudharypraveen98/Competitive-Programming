## [Transpose and Flatten](https://www.hackerrank.com/challenges/np-transpose-and-flatten)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        96.88% |

[**Transpose**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html#numpy-transpose) 


We can generate the transposition of an array using the tool `numpy.transpose`.   

It will not affect the original array, but it will create a new array.



```
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]

```

[**Flatten**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html)


The tool *flatten* creates a copy of the input array flattened to one dimension.



```
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]

```



---


**Task** 


You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).   

Your task is to print the *transpose* and *flatten* results.

**Input Format**

The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.
**Output Format**

First, print the *transpose* array and then print the *flatten*.

**Sample Input**


```
2 2
1 2
3 4

```
**Sample Output**


```
[[1 3]
 [2 4]]
[1 2 3 4]

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Transpose and Flatten](./transpose_and_flatten.py)

| Submissions                                                                                   |                                            Leaderboard                                             |                                                                                   Discussions |                                                                               Editorial |
| :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-transpose-and-flatten/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-transpose-and-flatten/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-transpose-and-flatten/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-transpose-and-flatten/editorial) |

