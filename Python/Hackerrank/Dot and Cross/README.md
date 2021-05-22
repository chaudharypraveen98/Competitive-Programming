## **[Dot and Cross](https://www.hackerrank.com/challenges/np-dot-and-cross)**


**dot**
The dot tool returns the dot product of two arrays.
```
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
```

**cross**  
The cross tool returns the cross product of two arrays.
```
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
```

##### Input Format

The first line contains the integer **N**.
The next **N** lines contains **N** space separated integers of array **A**.
The following **N** lines contains **N** space separated integers of array **B**.

#### Output Format

Print the matrix multiplication of  and .


**Sample Input 0**  
```
2
1 2
3 4
1 2
3 4
```

**Sample Output 0**  
```
[[ 7 10]
 [15 22]]
```