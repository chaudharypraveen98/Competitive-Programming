## **[Company Logo](https://www.hackerrank.com/challenges/most-commons)** 
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string **S**, which is the company name in lowercase letters, your task is to find the top three most common characters in the string. 
<ul>
<li>Print the three most common characters along with their occurrence count.</li>
<li>Sort in descending order of occurrence count.</li>
<li>If the occurrence count is the same, sort the characters in alphabetical order.</li>
</ul>

**Sample Input 0**  
`aabbbccde`

**Sample Output 0**   
```
b 3
a 2
c 2
```

**Explanation 0**  
Here, b occurs **3** times. It is printed first.
Both a and c occur **2** times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string **S** has at least **3** distinct characters.
