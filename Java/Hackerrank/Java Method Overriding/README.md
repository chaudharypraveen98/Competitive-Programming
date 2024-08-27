## [Java Method Overriding](https://www.hackerrank.com/challenges/java-method-overriding)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 98.83%        |

When a subclass inherits from a superclass, it also inherits its methods; however, it can also *override* the superclass methods (as well as declare and implement new ones). Consider the following *Sports* class:



```
class Sports{
    String getName(){
        return "Generic Sports";
    }
    void getNumberOfTeamMembers(){
        System.out.println( "Each team has n players in " + getName() );
    }
}

```

Next, we create a *Soccer* class that inherits from the *Sports* class. We can override the *getName* method and return a different, subclass\-specific string:



```
class Soccer extends Sports{
    @Override
    String getName(){
        return "Soccer Class";
    }
}

```

**Note:** When overriding a method, you should precede it with the `@Override` annotation. The parameter(s) and return type of an overridden method must be exactly the same as those of the method inherited from the supertype. 




---


**Task**   

Complete the code in your editor by writing an overridden *getNumberOfTeamMembers* method that prints the same statement as the superclass' *getNumberOfTeamMembers* method, except that it replaces  *[SVG image]*  with  *[SVG image]*  (the number of players on a Soccer team). 

**Output Format**

When executed, your completed code should print the following:



```
Generic Sports
Each team has n players in Generic Sports
Soccer Class
Each team has 11 players in Soccer Class

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Method Overriding](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-method-overriding/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-method-overriding/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-method-overriding/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-method-overriding/editorial) |

