## [Concatenate](https://www.hackerrank.com/challenges/np-concatenate)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        98.56% |

[**Concatenate**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html) 


Two or more arrays can be concatenated together using the *concatenate* function with a
tuple of the arrays to be joined:



```
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]

```

If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.



```
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]    

```



---


**Task** 


You are given two integer arrays of size *N* X *P* and *M* X *P*( *N* & *M* are rows, and *P* is the column). Your task is to concatenate the arrays along axis *0*.

**Input Format**

The first line contains space separated integers  *[SVG image]* ,  *[SVG image]*  and  *[SVG image]* .   

The next  *[SVG image]*  lines contains the space separated elements of the  *[SVG image]*  columns.   

After that, the next  *[SVG image]*  lines contains the space separated elements of the  *[SVG image]*  columns.

**Output Format**

Print the concatenated array of size  *[SVG image]* X *[SVG image]* .

**Sample Input**


```
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

```
**Sample Output**


```
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Concatenate](./concatenate.py)

| Submissions                                                                         |                                       Leaderboard                                        |                                                                         Discussions |                                                                     Editorial |
| :---------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------: | ----------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-concatenate/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-concatenate/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-concatenate/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-concatenate/editorial) |

