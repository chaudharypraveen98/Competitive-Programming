## [Floor, Ceil and Rint](https://www.hackerrank.com/challenges/floor-ceil-and-rint)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        96.78% |

[**floor**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.floor.html#numpy-floor)   

The tool *floor* returns the floor of the input element\-wise.   

The floor of  *[SVG image]*  is the largest integer  *[SVG image]*  where  *[SVG image]* . 



```
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

```

[**ceil**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ceil.html#numpy-ceil)   

The tool *ceil* returns the ceiling of the input element\-wise.   

The ceiling of  *[SVG image]*  is the smallest integer  *[SVG image]*  where  *[SVG image]* . 



```
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

```

[**rint**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.rint.html)   

The *rint* tool rounds to the nearest integer of input element\-wise.



```
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

```



---


#### Task
You are given a 1-D array, `A`. Your task is to print the **floor**, **ceil** and **rint** of all the elements of A.

##### Note

In order to get the correct output format, add the line `numpy.set_printoptions(legacy='1.13')` below the numpy import.

#### Input Format

A single line of input containing the space separated elements of array A.

#### Output Format

On the first line, print the `floor` of A.
On the second line, print the `ceil` of A.
On the third line, print the `rint` of A.

#### Sample Input
```
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
```

#### Sample Output
```
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Floor, Ceil and Rint](./floor_ceil_and_rint.py)

| Submissions                                                                              |                                          Leaderboard                                          |                                                                              Discussions |                                                                          Editorial |
| :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/floor-ceil-and-rint/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/floor-ceil-and-rint/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/floor-ceil-and-rint/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/floor-ceil-and-rint/editorial) |

