## **[Collections.namedtuple()](https://www.hackerrank.com/challenges/py-collections-namedtuple)**

**collections.namedtuple()**

Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
**Example**  

Code 01
```
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```

Code 02  
```
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y

```
<strong><sub>Note: <br>
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet. <br>
2. Column names are <code>ID</code>, <code>MARKS</code>, <code>CLASS</code> and <code>NAME</code>. (The spelling and case type of these names won't change.)</sub></strong>

**Input Format**

The first line contains an integer **N**, the total number of students.
The second line contains the names of the columns in any order.
The next **N** lines contains the **marks** , *IDs* , **name** and **class**, under their respective column nam

**Output Format**

Print the average marks of the list corrected to 2 decimal places.

**Sample Input 0**  
`78.00`

**Sample Output 0**  
`81.00`

**Explanation 0**  
Average = ( 97 + 50 + 91 + 72 + 80)/5

Can you solve this challenge in 4 lines of code or less?

**NOTE**: There is no penalty for solutions that are correct but have more than 4 line
