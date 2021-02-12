## **[Merge the Tools!](https://www.hackerrank.com/challenges/merge-the-tools)** 

Consider the following:  
<ul>
<li>A string,`S` , of `n` length where S=C0C1...CN-1.</li>
<li>An integer, , where is a factor of .
</li>
</ul>  

We can split `S` into `n/k` substrings where each subtring,`t`i , consists of a contiguous block of ` k` characters in `S`. Then, use each ` t`i to create `u`i string such that:<br>

<ul>
<li>
The characters in are a subsequence of the characters in .
</li>
<li>
Any repeat occurrence of a character is removed from the string such that each character in occurs exactly once. In other words, if the character at some index in occurs at a previous index in , then do not include the character in string .
</li>
</ul>  

####Function Description  
Complete the merge_the_tools function in the editor below.  
merge_the_tools has the following parameters:  
<ul>
<li>string s: the string to analyze</li>
<li>int k: the size of substrings to analyze</li>
</ul>  

####Input Format  
The first line contains a single string,`S `.  
The second line contains an integer,`k `, the length of each substring.
   
**Sample Input 0**  
 STDIN       Function  
AABCAAADA   s = 'AABCAAADA'   
3 ----------------  k = 3  

**Sample Output 0** 
AB  
CA  
AD  
  