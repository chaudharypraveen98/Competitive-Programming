## **[Set Mutations](https://www.hackerrank.com/challenges/py-set-mutations)** 
We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.<br>We can use the following operations to create mutations to a set:<br><strong>.update()</strong> or <strong><code>|=</code></strong> <br>
Update the set by adding elements from an iterable/another set.<br><br><code>>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])</code><br><strong>.intersection_update()</strong> or <strong><code>&amp;=</code></strong><br>
Update the set by keeping only the elements found in it and an iterable/another set.<br><br><code>   
   
 
  
 </code><br><strong>.difference_update()</strong> or <strong><code>-=</code></strong><br>
Update the set by removing elements found in an iterable/another set.<br><br><code></code><br><strong>.symmetric_difference_update()</strong> or <strong><code>^=</code></strong><br>
Update the set by only keeping the elements found in either set, but not in both.<br><code></code><br><br><br><br>**Sample Input 0**<br><br>**Sample Output 0**<br><br>**Explanation 0**<br><br>