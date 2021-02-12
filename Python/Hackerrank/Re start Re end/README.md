## **[Re.start() & Re.end()](https://www.hackerrank.com/challenges/re-start-re-end)** 
These expressions return the indices of the start and end of the substring matched by the group.

Code
<p> >>> import re <br> 
>>> m = re.search(r'\d+','1234') <br> 
>>> m.end()  <br>
4 <br>
>>> m.start() <br>
0</p> 

**Task**

You are given a string .
Your task is to find the indices of the start and end of string in .

**Sample Input 0**<br>aaadaa<br>
aa

**Sample Output 0**  
(0, 1)  
(1, 2)  
(4, 5)