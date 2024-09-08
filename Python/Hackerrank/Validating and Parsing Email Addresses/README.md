## [Validating and Parsing Email Addresses](https://www.hackerrank.com/challenges/validating-named-email-addresses)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
| :--------- | :-------: | ------------: |
| Easy       |    20     |        93.43% |

A valid email address meets the following criteria: 


* It's composed of a *username*, *domain* name, and *extension* assembled in this format: `username@domain.extension`
* The *username* starts with an *English alphabetical character*, and any subsequent characters consist of one or more of the following: [alphanumeric characters](https://en.wikipedia.org/wiki/Alphanumeric), `-`,`.`, and `_`.
* The *domain* and *extension* contain only [English alphabetical characters](https://en.wikipedia.org/wiki/English_alphabet).
* The *extension* is  *[SVG image]* ,  *[SVG image]* , or  *[SVG image]*  characters in length.


Given  *n*  pairs of names and email addresses as input, print each name and email address pair having a *valid* email address on a new line.


**Hint:** Try using [Email.utils()](https://docs.python.org/2/library/email.util.html#module-email.utils) to complete this challenge. For example, this code: 



```
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))

```

produces this output:



```
('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>

```
**Input Format**

The first line contains a single integer, **n**, denoting the number of email address.
Each line **i** of the **n** subsequent lines contains a name and an email address as two space-separated values following this format:



```
name <user@email.com>

```
**Constraints**

* *[SVG image]*
**Output Format**

Print the space\-separated name and email address pairs containing *valid* email addresses only. Each pair must be printed on a new line in the following format:



```
name <user@email.com>

```

You must print each valid email address in the same order as it was received as input.

**Sample Input**


```
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

```
**Sample Output**


```
DEXTER <dexter@hotmail.com>

```
**Explanation**

*dexter@hotmail.com* is a valid email address, so we print the name and email address pair received as input on a new line.   

*virus!@variable.:p* is not a valid email address because the username contains an exclamation point (`!`) and the extension contains a colon (`:`). As this email is not valid, we print nothing.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Validating and Parsing Email Addresses](./validating_and_parsing_email_addresses.py)

| Submissions                                                                                           |                                                Leaderboard                                                 |                                                                                           Discussions |                                                                                       Editorial |
| :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------------: |
| [📝 My Submission](https://www.hackerrank.com/challenges/validating-named-email-addresses/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/validating-named-email-addresses/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/validating-named-email-addresses/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/validating-named-email-addresses/editorial) |

