## **[Classes: Dealing with Complex Numbers](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers)** 

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.
<br>Input Format<br>One line of input: The real and imaginary part of a number separated by a space.

Output Format<br>For two complex numbers and , the output should be in the following sequence on separate lines:

#### Sample Input
```
2 1
5 6
```

#### Sample Output
```
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
```

#### Concept  
Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here.

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

```
__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation
```