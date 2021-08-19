## **[Polar Coordinates](https://www.hackerrank.com/challenges/polar-coordinates)** 
Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

A complex number `z=x+ij` is completely determined by its real part  and imaginary part .
Here, `j` is the imaginary unit.
A polar coordinate () 
<img src="https://s3.amazonaws.com/hr-challenge-images/9951/1440141121-5b051fd241-Capture.PNG" title="Capture.PNG">

is completely determined by modulus  and phase angle .

If we convert complex number  to its polar coordinate, we find:
: Distance from  to origin, i.e., 
: Counter clockwise angle measured from the positive -axis to the line segment that joins  to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.


This tool returns the phase of complex number  (also known as the argument of `z`).
```
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
```

This tool returns the modulus (absolute value) of complex number `z`.
```
>>> abs(complex(-1.0, 0.0))
1.0
```

#### Task
You are given a complex `z`. Your task is to convert it to polar coordinates.

#### Input Format

A single line containing the complex number `z`. Note: complex() function can be used in python to convert the input as a complex number.

#### Constraints

Given number is a valid complex number `z`

#### Output Format

Output two lines:
The first line should contain the value of `r`.
The second line should contain the value of `q`.

#### Sample Input
```
1+2j
```

#### Sample Output
```
2.23606797749979 
1.1071487177940904
```
Note: The output should be correct up to 3 decimal places.