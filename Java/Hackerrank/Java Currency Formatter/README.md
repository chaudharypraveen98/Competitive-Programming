## [Java Currency Formatter](https://www.hackerrank.com/challenges/java-currency-formatter)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 15      | 96.51%        |

Given a [double\-precision](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) number,  *[SVG image]* , denoting an amount of money, use the [NumberFormat](https://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html) class' [getCurrencyInstance](https://docs.oracle.com/javase/8/docs/api/java/text/NumberFormat.html#getCurrencyInstance-java.util.Locale-) method to convert  *[SVG image]*  into the US, Indian, Chinese, and French currency formats. Then print the formatted values as follows:



```
US: formattedPayment
India: formattedPayment
China: formattedPayment
France: formattedPayment

```

where  *[SVG image]*  is  *[SVG image]*  formatted according to the appropriate [Locale](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html)'s currency.


**Note:** India does not have a built\-in Locale, so you must [construct one](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html#Locale-java.lang.String-java.lang.String-) where the language is `en` (i.e., English).

**Input Format**

A single double\-precision number denoting  *[SVG image]* .

**Constraints**

* *[SVG image]*
**Output Format**

On the first line, print `US: u` where  *[SVG image]*  is  *[SVG image]*  formatted for US currency.   

On the second line, print `India: i` where  *[SVG image]*  is  *[SVG image]*  formatted for Indian currency.   

On the third line, print `China: c` where  *[SVG image]*  is  *[SVG image]*  formatted for Chinese currency.   

On the fourth line, print `France: f`, where  *[SVG image]*  is  *[SVG image]*  formatted for French currency.

**Sample Input**


```
12324.134

```
**Sample Output**


```
US: $12,324.13
India: Rs.12,324.13
China: ￥12,324.13
France: 12 324,13 €

```
**Explanation**

Each line contains the value of  *[SVG image]*  formatted according to the four countries' respective currencies.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Currency Formatter](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-currency-formatter/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-currency-formatter/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-currency-formatter/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-currency-formatter/editorial) |

