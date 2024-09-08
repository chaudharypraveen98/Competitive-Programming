## [Polar Coordinates](https://www.hackerrank.com/challenges/polar-coordinates)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    10     |        96.58% |

[**Polar coordinates**](https://en.wikipedia.org/wiki/Polar_coordinate_system) are an alternative way of representing Cartesian coordinates or [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number).


A complex number `z=x+ij` is completely determined by its real part  and imaginary part . 

Here, `j` is the imaginary unit.
A polar coordinate ( *[SVG image]* )
![](https://s3.amazonaws.com/hr-challenge-images/9951/1440141121-5b051fd241-Capture.PNG "Capture.PNG")


is completely determined by modulus  *[SVG image]*  and phase angle  *[SVG image]* .  
  

If we convert complex number  *[SVG image]*  to its polar coordinate, we find:  

 *[SVG image]* : Distance from  *[SVG image]*  to origin, i.e.,  *[SVG image]*   

 *[SVG image]* : Counter clockwise angle measured from the positive  *[SVG image]* \-axis to the line segment that joins  *[SVG image]*  to the origin.


Python's [cmath](https://docs.python.org/2/library/cmath.html) module provides access to the mathematical functions for complex numbers.


 *[SVG image]*    

This tool returns the phase of complex number  *[SVG image]*  (also known as the argument of `z`).



```
>>> phase(complex(-1.0, 0.0))
3.1415926535897931

```

 *[SVG image]*    


This tool returns the modulus (absolute value) of complex number `z`.



```
>>> abs(complex(-1.0, 0.0))
1.0

```

**Task**   

You are given a complex `z`. Your task is to convert it to polar coordinates.

**Input Format**
A single line containing the complex number `z`. Note: complex() function can be used in python to convert the input as a complex number.

**Constraints**

Given number is a valid complex number `z`

**Output Format**

Output two lines:
The first line should contain the value of `r`.
The second line should contain the value of `q`.

**Sample Input**


```
  1+2j

```
**Sample Output**


```
 2.23606797749979 
 1.1071487177940904

```

**`Note: The output should be correct up to 3 decimal places.`** 


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Polar Coordinates](./polar_coordinates.py)

| Submissions                                                                            |                                         Leaderboard                                         |                                                                            Discussions |                                                                        Editorial |
| :------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/polar-coordinates/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/polar-coordinates/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/polar-coordinates/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/polar-coordinates/editorial) |

