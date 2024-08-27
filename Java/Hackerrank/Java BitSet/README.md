## [Java BitSet](https://www.hackerrank.com/challenges/java-bitset)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 20      | 97.35%        |

Java's [BitSet](https://docs.oracle.com/javase/7/docs/api/java/util/BitSet.html) class implements a vector of bit values (i.e.:  *[SVG image]*  ( *[SVG image]* ) or  *[SVG image]*  ( *[SVG image]* )) that grows as needed, allowing us to easily manipulate bits while optimizing space (when compared to other collections). Any element having a bit value of  *[SVG image]*  is called a *set bit*.


Given  *[SVG image]*  BitSets,  *[SVG image]*  and  *[SVG image]* , of size  *[SVG image]*  where all bits in both BitSets are initialized to  *[SVG image]* , perform a series of  *[SVG image]*  operations. After each operation, print the number of *set bits* in the respective BitSets as two space\-separated integers on a new line.

**Input Format**

The first line contains  *[SVG image]*  space\-separated integers,  *[SVG image]*  (the length of both BitSets  *[SVG image]*  and  *[SVG image]* ) and  *[SVG image]*  (the number of operations to perform), respectively.   

The  *[SVG image]*  subsequent lines each contain an operation in one of the following forms:


* [AND](https://en.wikipedia.org/wiki/Logical_conjunction)  *[SVG image]*
* [OR](https://en.wikipedia.org/wiki/Logical_disjunction)  *[SVG image]*
* [XOR](https://en.wikipedia.org/wiki/Exclusive_or)  *[SVG image]*
* [FLIP](https://en.wikipedia.org/wiki/Bitwise_operation#NOT) *[SVG image]*
* [SET](https://docs.oracle.com/javase/7/docs/api/java/util/BitSet.html#set%28int%29)  *[SVG image]*


In the list above,  *[SVG image]*  is the integer  *[SVG image]*  or  *[SVG image]* , where  *[SVG image]*  denotes  *[SVG image]*  and  *[SVG image]*  denotes  *[SVG image]* .   

 *[SVG image]*  is an integer denoting a bit's index in the BitSet corresponding to  *[SVG image]* . 


For the binary operations  *[SVG image]* ,  *[SVG image]* , and  *[SVG image]* , operands are read from left to right and the BitSet resulting from the operation replaces the contents of the *first operand*. For example:



```
AND 2 1

```

 *[SVG image]*  is the left operand, and  *[SVG image]*  is the right operand. This operation should assign the result of  *[SVG image]*  to  *[SVG image]* . 


**Constraints**


* *[SVG image]*
* *[SVG image]*
**Output Format**

After each operation, print the respective number of *set bits* in BitSet  *[SVG image]*  and BitSet  *[SVG image]*  as  *[SVG image]*  space\-separated integers on a new line.

**Sample Input**


```
5 4
AND 1 2
SET 1 4
FLIP 2 2
OR 2 1

```
**Sample Output**


```
0 0
1 0
1 1
1 2

```
**Explanation**

Initially:  *[SVG image]* ,  *[SVG image]* ,  *[SVG image]* , and  *[SVG image]* . At each step, we print the respective number of *set bits* in  *[SVG image]*  and  *[SVG image]*  as a pair of space\-separated integers on a new line.


 *[SVG image]*    

 *[SVG image]*    

 *[SVG image]* ,  *[SVG image]*    

The number of *set bits* in  *[SVG image]*  and  *[SVG image]*  is  *[SVG image]* .


 *[SVG image]*    

Set  *[SVG image]*  to  *[SVG image]*  ( *[SVG image]* ).   

 *[SVG image]* ,  *[SVG image]* .   

The number of *set bits* in  *[SVG image]*  is  *[SVG image]*  and  *[SVG image]*  is  *[SVG image]* .


 *[SVG image]*    

Flip  *[SVG image]*  from  *[SVG image]*  ( *[SVG image]* ) to  *[SVG image]*  ( *[SVG image]* ).   

 *[SVG image]* ,  *[SVG image]* .   

The number of *set bits* in  *[SVG image]*  is  *[SVG image]*  and  *[SVG image]*  is  *[SVG image]* .


 *[SVG image]*    

 *[SVG image]* .   

 *[SVG image]* ,  *[SVG image]* .   

The number of *set bits* in  *[SVG image]*  is  *[SVG image]*  and  *[SVG image]*  is  *[SVG image]* .


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java BitSet](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-bitset/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-bitset/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-bitset/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-bitset/editorial) |

