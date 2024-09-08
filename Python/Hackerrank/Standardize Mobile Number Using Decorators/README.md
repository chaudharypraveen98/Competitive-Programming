## [Standardize Mobile Number Using Decorators](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    30     |        97.51% |

Let's dive into decorators! You are given **N** mobile numbers. Sort them in ascending order then print them in the standard format shown below:  
  




```
+91 xxxxx xxxxx

```

  
The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.
  



**Input Format**


The first line of input contains an integer **N**, the number of mobile phone numbers.
**N** lines follow each containing a mobile number.


**Output Format**


Print **N** mobile numbers on separate lines in the required format.


**Sample Input**



```
3
07895462130
919875641230
9195969878

```

**Sample Output**



```
+91 78954 62130
+91 91959 69878
+91 98756 41230

```

**Concept**


Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps [here](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/).  

To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Standardize Mobile Number Using Decorators](./standardize_mobile_number_using_decorators.py)

| Submissions                                                                                                     |                                                     Leaderboard                                                      |                                                                                                     Discussions |                                                                                                 Editorial |
| :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/editorial) |

