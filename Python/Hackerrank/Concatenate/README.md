## **[Concatenate](https://www.hackerrank.com/challenges/np-concatenate)** 
Concatenate<br>Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:

```
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]
```

If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

```
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]
```

#### Task
You are given two integer arrays of size *N* X *P* and *M* X *P*( *N* & *M* are rows, and *P* is the column). Your task is to concatenate the arrays along axis *0*.


**Sample Input 0**  
```
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
```

**Sample Output 0**  
```
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
```