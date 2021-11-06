## **[C++ Class Template Specialization](https://www.hackerrank.com/challenges/cpp-class-template-specialization)** 
You are given a main function which reads the enumeration values for two different types as input, then prints out the corresponding enumeration names. Write a class template that can provide the names of the enumeration values for both types. If the enumeration value is not valid, then print unknown.

##### Input Format

The first line contains t, the number of test cases.
Each of the t subsequent lines contains two space-separated integers. 
The first integer is a color value, c , and the second integer is a fruit value, f.


#### Output Format

The locked stub code in your editor prints  lines containing the color name and the fruit name corresponding to the input enumeration index.

#### Sample Input
```
2
1 0
3 3
```

#### Sample Output
```
green apple
unknown unknown
```

#### Explanation

Since t= 2, there are two lines of output.

The two input index values, 1 and , 1correspond to green in the color enumeration and apple in the fruit enumeration. Thus, we print green apple.
The two input values, 3 and 3, are outside of the range of our enums. Thus, we print unknown unknown.