## [Zeros and Ones](https://www.hackerrank.com/challenges/np-zeros-and-ones)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        95.22% |

**[zeros](http://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html#numpy-zeros)**


The *zeros* tool returns a new array with a given shape and type filled with  *0* 's.



```
import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]

```

**[ones](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html#numpy-ones)**


The *ones* tool returns a new array with a given shape and type filled with  *1*'s.



```
import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]   

```



---


**Task** 


You are given the shape of the array in the form of space\-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools `numpy.zeros` and `numpy.ones`.

**Input Format**

A single line containing the space\-separated integers.

**Constraints**

 *[SVG image]* 

**Output Format**

First, print the array using the `numpy.zeros` tool and then print the array with the `numpy.ones` tool. 

**Sample Input 0**


```
3 3 3

```

**Sample Output 0**


```
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]

```

**Explanation 0**

Print the array built using `numpy.zeros` and `numpy.ones` tools and you get the result as shown. 


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Zeros and Ones](./zeros_and_ones.py)

| Submissions                                                                            |                                         Leaderboard                                         |                                                                            Discussions |                                                                        Editorial |
| :------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-zeros-and-ones/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-zeros-and-ones/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-zeros-and-ones/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-zeros-and-ones/editorial) |

