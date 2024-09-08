## [Athlete Sort](https://www.hackerrank.com/challenges/python-sort-sort)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Medium     |    30     |        95.50% |

You are given a spreadsheet that contains a list of  athletes athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the  *K*th attribute and print the final resulting table. Follow the example given below for better understanding. 


![image](https://s3.amazonaws.com/hr-assets/0/1514874268-6fabad07aa-AthleteSort2.png)


Note that  is indexed from  to , where  is the number of attributes. 


**Note**: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

**Input Format**

The first line contains  *N*  and  *M*  separated by a space.   

The next  *N*  lines each contain  *M*  elements.   

The last line contains  *K* . 

**Constraints**

 *[SVG image]*    

 *[SVG image]*    

Each element  *[SVG image]* 

**Output Format**

Print the  *N*  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity. 

**Sample Input 0**


```
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

```

**Sample Output 0**


```
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

```

**Explanation 0**

The details are sorted based on the second attribute, since  *K*  is zero-indexed. 


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Athlete Sort](./athlete_sort.py)

| Submissions                                                                           |                                        Leaderboard                                         |                                                                           Discussions |                                                                       Editorial |
| :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/python-sort-sort/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/python-sort-sort/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/python-sort-sort/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/python-sort-sort/editorial) |

