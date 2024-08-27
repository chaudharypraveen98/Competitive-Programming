## [Java Stdin and Stdout I](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 5      | 96.83%        |

Most HackerRank challenges require you to read input from [stdin](https://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29) (standard input) and write output to [stdout](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29) (standard output).


One popular way to read input from stdin is by using the [Scanner class](https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html) and specifying the *Input Stream* as *System.in*. For example:



```
Scanner scanner = new Scanner(System.in);
String myString = scanner.next();
int myInt = scanner.nextInt();
scanner.close();

System.out.println("myString is: " + myString);
System.out.println("myInt is: " + myInt);

```

The code above creates a *Scanner* object named  *[SVG image]*  and uses it to read a *String* and an *int*. It then *closes* the *Scanner* object because there is no more input to read, and prints to stdout using *System.out.println(String)*. So, if our input is:



```
Hi 5

```

Our code will print:



```
myString is: Hi
myInt is: 5

```

Alternatively, you can use the [BufferedReader class](https://docs.oracle.com/javase/8/docs/api/java/io/BufferedReader.html).


**Task**   

In this challenge, you must read  *[SVG image]*  integers from stdin and then print them to stdout. Each integer must be printed on a new line. To make the problem a little easier, a portion of the code is provided for you in the editor below.

**Input Format**

There are  *[SVG image]*  lines of input, and each line contains a single integer.

**Sample Input**


```
42
100
125

```
**Sample Output**


```
42
100
125

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Stdin and Stdout I](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/editorial) |

