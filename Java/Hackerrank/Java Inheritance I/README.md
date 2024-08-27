## [Java Inheritance I](https://www.hackerrank.com/challenges/java-inheritance-1)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 5      | 98.20%        |

Using *inheritance*, one class can acquire the properties of others. Consider the following *Animal* class:



```
class Animal{
    void walk(){
        System.out.println("I am walking");
    }
}

```

This class has only one method, *walk*. Next, we want to create a *Bird* class that also has a *fly* method. We do this using *extends* keyword:



```
class Bird extends Animal {
    void fly() {
        System.out.println("I am flying");
    }
}

```

Finally, we can create a Bird object that can both *fly* and *walk*.



```
public class Solution{
   public static void main(String[] args){

      Bird bird = new Bird();
      bird.walk();
      bird.fly();
   }
}

```

The above code will print:



```
I am walking
I am flying

```

This means that a Bird object has all the properties that an Animal object has, as well as some additional unique properties.


The code above is provided for you in your editor. You must add a *sing* method to the *Bird* class, then modify the *main* method accordingly so that the code prints the following lines:



```
I am walking
I am flying
I am singing

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Inheritance I](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-inheritance-1/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-inheritance-1/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-inheritance-1/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-inheritance-1/editorial) |

