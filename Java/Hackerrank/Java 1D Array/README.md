## [Java 1D Array](https://www.hackerrank.com/challenges/java-1d-array-introduction)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 5      | 97.29%        |

An array is a simple data structure used to store a collection of data in a contiguous block of memory. Each element in the collection is accessed using an *index*, and the elements are easy to find because they're stored sequentially in memory. 


Because the collection of elements in an array is stored as a big block of data, we typically use arrays when we know exactly how many pieces of data we're going to have. For example, you might use an array to store a list of student ID numbers, or the names of state capitals. To create an array of integers named  *[SVG image]*  that can hold four integer values, you would write the following code:



```
int[] myArray = new int[4];

```

This sets aside a block of memory that's capable of storing  *[SVG image]*  integers. Each integer storage cell is assigned a unique *index* ranging from  *[SVG image]*  to one less than the size of the array, and each cell initially contains a  *[SVG image]* . In the case of  *[SVG image]* , we can store integers at indices  *[SVG image]* ,  *[SVG image]* ,  *[SVG image]* , and  *[SVG image]* . Let's say we wanted the last cell to store the number  *[SVG image]* ; to do this, we write:



```
myArray[3] = 12;

```

Similarly, we can print the contents of the last cell with the following code:



```
System.out.println(myArray[3]);

```

The code above prints the value stored at index  *[SVG image]*  of  *[SVG image]* , which is  *[SVG image]*  (the value we previously stored there). It's important to note that while Java initializes each cell of an array of integers with a  *[SVG image]* , not all languages do this.


**Task** 


The code in your editor does the following:


1. Reads an integer from stdin and saves it to a variable,  *[SVG image]* , denoting some number of integers.
2. Reads  *[SVG image]*  integers corresponding to  *[SVG image]*  from stdin and saves each integer  *[SVG image]*  to a variable,  *[SVG image]* .
3. Attempts to print each element of an array of integers named  *[SVG image]* .


Write the following code in the unlocked portion of your editor:


1. Create an array,  *[SVG image]* , capable of holding  *[SVG image]*  integers.
2. Modify the code in the loop so that it saves each sequential value to its corresponding location in the array. For example, the first value must be stored in  *[SVG image]* , the second value must be stored in  *[SVG image]* , and so on.


Good luck!

**Input Format**

The first line contains a single integer,  *[SVG image]* , denoting the size of the array.   

Each line  *[SVG image]*  of the  *[SVG image]*  subsequent lines contains a single integer denoting the value of element  *[SVG image]* .

**Output Format**

You are not responsible for printing any output to stdout. Locked code in the editor loops through array  *[SVG image]*  and prints each sequential element on a new line.

**Sample Input**


```
5
10
20
30
40
50

```
**Sample Output**


```
10
20
30
40
50

```
**Explanation**

When we save each integer to its corresponding index in  *[SVG image]* , we get  *[SVG image]* . The locked code prints each array element on a new line from left to right.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java 1D Array](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-1d-array-introduction/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-1d-array-introduction/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-1d-array-introduction/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-1d-array-introduction/editorial) |

