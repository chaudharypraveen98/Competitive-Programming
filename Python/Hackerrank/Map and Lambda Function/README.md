## [Map and Lambda Function](https://www.hackerrank.com/challenges/map-and-lambda-expression)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        95.27% |

Let's learn some new Python concepts! You have to generate a list of the first **N** fibonacci numbers, **0** being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.


**Concept**


The `map()` function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.   

Let's say you are given a list of names, and you have to print a list that contains the length of each name. 



```
>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  

```

*Lambda* is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming. 



```
>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6

```

**Note:** 


*Lambda* functions cannot use the return statement and can only have a single expression. Unlike *def*, which creates a function and assigns it a name, *lambda* creates a function and returns the function itself. Lambda can be used inside lists and dictionaries. 

**Input Format**

One line of input: an integer **N**

**Constraints** 


 *[SVG image]*  

**Output Format**

A list on a single line containing the cubes of the first **N** fibonacci numbers.


**Sample Input**


```
5

```
**Sample Output**


```
[0, 1, 1, 8, 27]

```
**Explanation**

The first 5 fibonacci numbers are [0,1,1,2,3], and their cubes are [0,1,1,8,27]


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Map and Lambda Function](./map_and_lambda_function.py)

| Submissions                                                                                    |                                             Leaderboard                                             |                                                                                    Discussions |                                                                                Editorial |
| :--------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/map-and-lambda-expression/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/map-and-lambda-expression/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/map-and-lambda-expression/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/map-and-lambda-expression/editorial) |

