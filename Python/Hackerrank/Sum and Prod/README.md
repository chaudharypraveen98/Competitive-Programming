## [Sum and Prod](https://www.hackerrank.com/challenges/np-sum-and-prod)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        98.06% |

 [**sum**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html)  


The *sum* tool returns the sum of array elements over a given axis. 



```
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10

```

By default, the axis value is `None`. Therefore, it performs a sum over all the dimensions of the input array.


[**prod**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.prod.html)


The *prod* tool returns the product of array elements over a given axis. 



```
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24

```

By default, the axis value is `None`. Therefore, it performs the product over all the dimensions of the input array.




---


**Task** 


You are given a 2\-D array with dimensions N X M.

Your task is to perform the **SUM** tool over axis 0 and then find the **product** of that result.

**Input Format**

The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

**Output Format**

Compute the sum along axis 0. Then, print the product of that sum.

**Sample Input**


```
2 2
1 2
3 4

```
**Sample Output**


```
24

```
**Explanation**
The sum along axis 0 = [4,6 ]
The product of this sum = 24 


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Sum and Prod](./sum_and_prod.py)

| Submissions                                                                          |                                        Leaderboard                                        |                                                                          Discussions |                                                                      Editorial |
| :----------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------: | -----------------------------------------------------------------------------------: | -----------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-sum-and-prod/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-sum-and-prod/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-sum-and-prod/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-sum-and-prod/editorial) |

