You are given two tables: Students and Grades. 
Students contains three columns ID, Name and Marks.

<img src="res/1.png">

Grades contains the following data:

<img src="res/2.png">

Ketty gives Eve a task to generate a report containing three 
columns: Name, Grade and Mark. Ketty doesn't want the NAMES
of those students who received a grade lower than 8. The
report must be in descending order by grade -- i.e. higher
grades are entered first. If there is more than one student
with the same grade (8-10) assigned to them, order those 
particular students by their name alphabetically. Finally,
if the grade is lower than 8, use "NULL" as their name and
list them by their grades in descending order. If there is
more than one student with the same grade (1-7) assigned to
them, order those particular students by their marks in ascending order.

Write a query to help Eve.

**Sample Input**

<img src="res/3.png">

**Sample Output**

```
Maria 10 99
Jane 9 81
Julia 9 88
Scarlet 8 78
NULL 7 63
NULL 7 68
```

**Note**

Print "NULL"  as the name if the grade is less than 8.

**Explanation**

Consider the following table with the grades assigned to the students:

<img src="res/4.png">

So, the following students got 8, 9 or 10 grades:

- Maria (grade 10)
- Jane (grade 9)
- Julia (grade 9)
- Scarlet (grade 8)

