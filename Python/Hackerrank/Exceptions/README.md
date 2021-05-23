## **[Exceptions](https://www.hackerrank.com/challenges/exceptions)**   

Errors detected during execution are called exceptions.<br>**Example**s:
ZeroDivisionError
This error is raised when the second argument of a division or modulo operation is zero.<br>
```
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
```

ValueError

This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

```
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
```

#### Handling Exceptions
The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.
```
#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
```

##### Output

Error Code: integer division or modulo by zero

#### Task
You are given two values *a* and *b*.
Perform integer division and print *a/b*.

##### Sample Input
```
3
1 0
2 $
3 1
```

**Sample Output 0**  
```
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
```

<strong>Note:</strong> <br>
For integer division in <strong>Python 3</strong> use <code>//</code>.
</sub><br><br>