## [Linear Algebra](https://www.hackerrank.com/challenges/np-linear-algebra)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        94.58% |

The *NumPy* module also comes with a number of built\-in routines for linear algebra calculations. These can be found in the sub\-module *linalg*. 


[**linalg.det**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html)


The *linalg.det* tool computes the determinant of an array. 



```
print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

```



---


[**linalg.eig**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html)


The *linalg.eig* computes the eigenvalues and right eigenvectors of a square array. 



```
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]

```



---


[**linalg.inv**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html) 


The *linalg.inv* tool computes the (multiplicative) inverse of a matrix.



```
print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]

```

Other routines can be found [here](http://docs.scipy.org/doc/numpy/reference/routines.linalg.html)




---


**Task**



You are given a square matrix **A** with dimensions **N X N**. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

**Input Format**

The first line contains the integer **N**.
The next **N** lines contains the **N** space separated elements of array **A**.

**Output Format**

Print the determinant of **A**.

**Sample Input**


```
2
1.1 1.1
1.1 1.1

```
**Sample Output**


```
0.0

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Linear Algebra](./linear_algebra.py)

| Submissions                                                                            |                                         Leaderboard                                         |                                                                            Discussions |                                                                        Editorial |
| :------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/np-linear-algebra/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/np-linear-algebra/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/np-linear-algebra/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/np-linear-algebra/editorial) |

