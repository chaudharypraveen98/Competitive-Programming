## **[Text Alignment](https://www.hackerrank.com/challenges/text-alignment)** 
In Python, a string of text can be aligned left, right and center.  
#### .ljust(width)

This method returns a left aligned string of length width.
```
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
```
#### .center(width)

This method returns a centered string of length width.
```
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
```
#### .rjust(width)
This method returns a right aligned string of length width.
```
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
```

#### Input Format

A single line containing the thickness value for the logo.

#### Constraints
The thickness must be an odd number.

#### Output Format

Output the desired logo.

#### Task
You are given a partial code that is used for generating the <em>HackerRank Logo</em> of variable <em>thickness</em>.
Your task is to replace the blank (<code>______</code>) with <em>rjust, ljust</em> or <em>center</em>.

**Sample Input 0**  
`5`  

**Sample Output 0**  
```
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
```