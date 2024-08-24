Query the two cities in **STATION** with the shortest and longest **CITY** names, 
as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes
first when ordered alphabetically.

The **STATION** table is described as follows:

<img src="res/1.jpg">


where **LAT_N** is the northern latitude and **LONG_W** is the western longitude.

**Sample Input**

For example, **CITY** has four entries: **DEF, ABC, PQRS and WXY.**

**Sample Output**

```
ABC 3
PQRS 4
```

**Explanation**


When ordered alphabetically, the **CITY** names are listed as **ABC, DEF, PQRS, and WXY,**
with lengths 3,3,4 and 3. The longest name is **PQRS**, but there are 3 options for shortest 
named city. Choose **ABC**, because it comes first alphabetically.

**Note**
You can write two separate queries to get the desired output. It need not be a single query.