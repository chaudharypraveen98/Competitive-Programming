## **[Reduce Function](https://www.hackerrank.com/challenges/reduce-function)** 
Given a list of rational numbers,find their product.<br><strong>Concept</strong> <br>
The <code>reduce()</code> function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say <code>[1,2,3]</code> and you have to find its sum.<br><code>>>> reduce(lambda x, y : x + y,[1,2,3])
6</code><br>You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:<br><code>>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

**Sample Input 0**  

**Sample Output 0**  

**Explanation 0**