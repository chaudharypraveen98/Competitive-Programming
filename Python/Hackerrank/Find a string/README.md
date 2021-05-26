## **[Find a string](https://www.hackerrank.com/challenges/find-a-string)** 
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 

**NOTE**: String letters are case-sensitive.

#### Input Format  
The first line of input contains the original string. The next line contains the substring.

#### Constraints  

Each character in the string is an ascii character.


#### Output Format  
Output the integer number indicating the total number of occurrences of the substring in the original string.

#### Sample Input  
```
ABCDCDC
CDC
```
#### Sample Output
`2`

Some string processing examples, <a href="http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation">such as these</a>, might be useful. <br>
There are a couple of new concepts: <br>
In Python, the length of a string is found by the function <code>len(s)</code>, where <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.09ex" height="1.676ex" style="vertical-align: -0.338ex;" viewBox="0 -576.1 469.5 721.6" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M131 289Q131 321 147 354T203 415T300 442Q362 442 390 415T419 355Q419 323 402 308T364 292Q351 292 340 300T328 326Q328 342 337 354T354 372T367 378Q368 378 368 379Q368 382 361 388T336 399T297 405Q249 405 227 379T204 326Q204 301 223 291T278 274T330 259Q396 230 396 163Q396 135 385 107T352 51T289 7T195 -10Q118 -10 86 19T53 87Q53 126 74 143T118 160Q133 160 146 151T160 120Q160 94 142 76T111 58Q109 57 108 57T107 55Q108 52 115 47T146 34T201 27Q237 27 263 38T301 66T318 97T323 122Q323 150 302 164T254 181T195 196T148 231Q131 256 131 289Z"></path></g></svg></span> is the string. <br>
To traverse through the length of a string, use a <em>for</em> loop: 
```
for i in range(0, len(s)):
    print (s[i])
```

A range function is used to loop over some length:
```
range (0, 5)
```

Here, the range loops over 0 to **4.5**  is excluded.