## **[Compress the String!](https://www.hackerrank.com/challenges/compress-the-string)** 
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .<br>You are given a string **S**. Suppose a character '**c**' occurs consecutively **x** times in the string. Replace these consecutive occurrences of the character '**c**' with in the string.<br>For a better understanding of the problem, check the explanation.

##### Input Format  
A single line of input consisting of the string `S`.

##### Output Format  
A single line of output consisting of the modified string.<br>

##### Constraints  
All the characters of **S** denote integers between *0* and *9*.

#### Sample Input
`1222311`

#### Sample Output
`(1, 1) (3, 2) (1, 3) (2, 1)`

First, the character **1** occurs only once. It is replaced by **(1,1)**. Then the character **2** occurs three times, and it is replaced by **(3,2)** and so on.

Also, note the single space within each compression and between the compressions.