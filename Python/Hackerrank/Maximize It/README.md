## **[Maximize It!](https://www.hackerrank.com/challenges/maximize-it)** 
You are given a function f(X)=X^2 . You are also given `K `lists. The `i'th` list consists of `N`i elements.<br>You have to pick one element from each list so that the value from the equation below is maximized:  
`S=(f(X1)+f(X2)+f()+....f(Xk))% M`<br>`X`i denotes the element picked from the list . Find the maximized value obtained.  
`%` denotes the modulo operator.<br>Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.  

**Sample Input 0**  
3 1000  
2 5 4  
3 7 8 9   
5 5 7 8 9 10  
 
**Sample Output 0**  
206  

**Explanation 0**  
Picking `5` from the `1`st list, `9` from the `2`nd list and `10` from the `3`rd list gives the maximum  `S` value equal to (`5`^2 + `9`^2 + `10`^2) % `1000`= 206.