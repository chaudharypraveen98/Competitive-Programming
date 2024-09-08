## [Classes: Dealing with Complex Numbers](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Medium       | 20      | 90.96%        |

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations. 


The real and imaginary precision part should be correct up to two decimal places.


**Input Format**


One line of input: The real and imaginary part of a number separated by a space.


**Output Format**


For two complex numbers  *[SVG image]*  and  *[SVG image]* , the output should be in the following sequence on separate lines:  



* *[SVG image]*
* *[SVG image]*
* *[SVG image]*
* *[SVG image]*
* *[SVG image]*
* *[SVG image]*


For complex numbers with non\-zero real *[SVG image]*  and complex part *[SVG image]* , the output should be in the following format:   

 *[SVG image]*   

Replace the plus symbol  *[SVG image]*  with a minus symbol  *[SVG image]*  when  *[SVG image]* .


For complex numbers with a zero complex part i.e. real numbers, the output should be:   

 *[SVG image]*  


For complex numbers where the real part is zero and the complex part *[SVG image]*  is non\-zero, the output should be:  

 *[SVG image]* 


**Sample Input**



```
2 1
5 6

```

**Sample Output**



```
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i

```

**Concept**


Python is a fully object\-oriented language like C\+\+, Java, etc. For reading about classes, refer [here](http://www.diveintopython3.net/iterators.html#defining-classes).
  
  

Methods with a double underscore before and after their name are considered as built\-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built\-in functionality.   




```
__add__-> Can be overloaded for + operation
```
  


```
__sub__ -> Can be overloaded for - operation
```
  


```
__mul__ -> Can be overloaded for * operation
```

  
  

For more information on operator overloading in Python, refer [here](http://docs.python.org/3.2/reference/datamodel.html).


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Classes: Dealing with Complex Numbers](./classes_dealing_with_complex_numbers.py)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/editorial) |

