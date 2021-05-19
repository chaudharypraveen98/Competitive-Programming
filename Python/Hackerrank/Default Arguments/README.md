## **[Default Arguments](https://www.hackerrank.com/challenges/default-arguments)** 
In this challenge, the task is to debug the existing code to successfully execute all provided test files.<br>Python supports a useful concept of default argument values. For each keyword argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it. For example, consider the following increment function:<br>
```
def increment_by(n, increment=1):
    return n + increment
```
The functions works like this:<br>
```
>>> increment_by(5, 2)
7
>>> increment_by(4)  
```
Debug the given function `print_from_stream` using the default value of one of its arguments. 

This function should print the first <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.395ex" height="1.676ex" style="vertical-align: -0.338ex;" viewBox="0 -576.1 600.5 721.6" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M21 287Q22 293 24 303T36 341T56 388T89 425T135 442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469 415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560 153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92 386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66 305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z"></path></g></svg></span> values returned by <code>get_next()</code> method of <code>stream</code> object provided as an argument. Each of these values should be printed in a separate line.<br>Whenever the function is called without the <code>stream</code> argument, it should use an instance of <code>EvenStream</code> class defined in the code stubs below as the value of <code>stream</code>.  

##### Input Format

The input is read by the provided locked code template. In the first line, there is a single integer **q** denoting the number of queries. Each of the following **q** lines contains a stream_name followed by integer **n**, and it corresponds to a single test for your function.

#### Output Format

The output is produced by the provided and locked code template. For each of the queries (stream_name, n), if the stream_name is even then print_from_stream(n) is called. Otherwise, if the stream_name is odd, then print_from_stream(n, OddStream()) is called.

**Sample Input 0**  
```
3
odd 2
even 3
odd 5
```

**Sample Output 0**  
```
1
3
0
2
4
1
3
5
7
9
```

**Explanation 0**  
There are `3` queries in the sample.

In the first query, the function print_from_stream(2, OddStream()) is exectuted, which leads to printing values **1** and **3** in separated lines as the first two non-negative odd numbers.

In the second query, the function print_from_stream(3) is exectuted, which leads to printing values **2**, **4** and **6** in separated lines as the first three non-negative even numbers.

In the third query, the function print_from_stream(5, OddStream()) is exectuted, which leads to printing values **1, 3, 5, 7** and **9** in separated lines as the first five non-negative odd numbers.