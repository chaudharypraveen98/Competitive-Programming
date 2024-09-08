## [Iterables and Iterators](https://www.hackerrank.com/challenges/iterables-and-iterators)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Medium     |    40     |        96.52% |

The *itertools* module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an *iterator algebra* making it possible to construct specialized tools succinctly and efficiently in pure *Python*. 


To read more about the functions in this module, check out their [documentation here](https://docs.python.org/2/library/itertools.html). 


You are given a list of **N** lowercase English letters. For a given integer **K**, you can select any **K** indices (assume 1-based indexing) with a uniform probability from the list.



Find the **probability** that **at least** one of the **K** indices selected will contain the letter: 'a'.


**Input Format**


The input consists of three lines. The first line contains the integer **N**, denoting the length of the list. The next line consists of **N** space-separated lowercase English letters, denoting the elements of the list. 

The third and the last line of input contains the integer **K**, denoting the number of indices to be selected.


**Output Format**


Output a single line consisting of the probability that at least one of the **K** indices selected contains the letter:'a'.

**Note**: The answer must be correct up to 3 decimal places. 


**Constraints**


 *[SVG image]* 


 *[SVG image]* 


*All the letters in the list are lowercase English letters.*


**Sample Input**



```
4 
a a c d
2

```

**Sample Output**



```
0.8333

```

**Explanation**
All possible unordered tuples of length  comprising of indices from  to  are:


Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.

Hence, the answer is 5/6.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Iterables and Iterators](./iterables_and_iterators.py)

| Submissions                                                                                  |                                            Leaderboard                                            |                                                                                  Discussions |                                                                              Editorial |
| :------------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/iterables-and-iterators/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/iterables-and-iterators/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/iterables-and-iterators/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/iterables-and-iterators/editorial) |

