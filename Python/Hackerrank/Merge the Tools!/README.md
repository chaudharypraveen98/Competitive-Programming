## [Merge the Tools!](https://www.hackerrank.com/challenges/merge-the-tools)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Medium     |    40     |        93.83% |

Consider the following:


* A string,  *[SVG image]* , of length  *[SVG image]*  where  *[SVG image]* .
* An integer,  *[SVG image]* , where  *[SVG image]*  is a factor of  *[SVG image]* .


We can split `S` into `n/k` substrings where each subtring,`t`i , consists of a contiguous block of ` k` characters in `S`. Then, use each ` t`i to create `u`i string such that:


* The characters in  *[SVG image]*  are a subsequence of the characters in  *[SVG image]* .
* Any repeat occurrence of a character is removed from the string such that each character in  *[SVG image]*  occurs exactly once. In other words, if the character at some index  *[SVG image]*  in  *[SVG image]*  occurs at a previous index  *[SVG image]*  in  *[SVG image]* , then do not include the character in string  *[SVG image]* .


Given  *[SVG image]*  and  *[SVG image]* , print  *[SVG image]*  lines where each line  *[SVG image]*  denotes string  *[SVG image]* . 


**Example**   

 *[SVG image]*    

 *[SVG image]*  


There are three substrings of length  *[SVG image]*  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so  *[SVG image]* . The second substring has all distinct characters, so  *[SVG image]* . The third substring has  *[SVG image]*  different characters, so  *[SVG image]* . Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important. 


**Function Description** 


Complete the *merge\_the\_tools* function in the editor below. 


*merge\_the\_tools* has the following parameters: 


* *string s:* the string to analyze
* *int k:* the size of substrings to analyze


**Prints** 


Print each subsequence on a new line. There will be  *[SVG image]*  of them. No return value is expected. 

**Input Format**
The first line contains a single string,`S `.  
The second line contains an integer,`k `, the length of each substring.
   

**Constraints**

* *[SVG image]* , where  *[SVG image]*  is the length of  *[SVG image]*
* *[SVG image]*
* It is guaranteed that  *[SVG image]*  is a multiple of  *[SVG image]* .
**Sample Input**


```
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

```
**Sample Output**


```
AB
CA
AD

```
**Explanation**

Split  *[SVG image]*  into  *[SVG image]*  equal parts of length  *[SVG image]* . Convert each  *[SVG image]*  to  *[SVG image]*  by removing any subsequent occurrences of non\-distinct characters in  *[SVG image]* :


1. *[SVG image]*
2. *[SVG image]*
3. *[SVG image]*


Print each  *[SVG image]*  on a new line.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Merge the Tools!](./merge_the_tools.py)

| Submissions                                                                          |                                        Leaderboard                                        |                                                                          Discussions |                                                                      Editorial |
| :----------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------: | -----------------------------------------------------------------------------------: | -----------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/merge-the-tools/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/merge-the-tools/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/merge-the-tools/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/merge-the-tools/editorial) |

