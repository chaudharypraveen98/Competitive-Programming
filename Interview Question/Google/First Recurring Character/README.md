## First Recurring Character  

<img src="find-first-repeated-character-in-a-string.png" alt="first-repeated">


**Simple Solution:** The solution is to run two nested loops. Start traversing from left side. For every character, check if it repeats or not. If the character repeats, increment count of repeating characters. When the count becomes K, return the character. 
Time Complexity of this solution is O(n2)

**An efficient solution is to use Hashing to solve this in O(N) time on average.** 

Create an empty hash.
Scan each character of input string and insert values to each keys in the hash.
When any character appears more than once, hash key value is increment by 1, and return the character.

#### Sample Input 0
`asdfghjkls`

#### Sample Output 0
`s`