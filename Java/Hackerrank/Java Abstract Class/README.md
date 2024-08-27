## [Java Abstract Class](https://www.hackerrank.com/challenges/java-abstract-class)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 10      | 98.56%        |

A Java abstract class is a class that can't be instantiated. That means you cannot create new instances of an abstract class. It works as a base for subclasses. You should learn about Java Inheritance before attempting this challenge. 


Following is an example of abstract class:



```
abstract class Book{
    String title;
    abstract void setTitle(String s);
    String getTitle(){
        return title;
    }
}

```

If you try to create an instance of this class like the following line you will get an error:



```
Book new_novel=new Book(); 

```

You have to create another class that extends the abstract class. Then you can create an instance of the new class. 


Notice that *setTitle* method is abstract too and has no body. That means you must implement the body of that method in the child class.


In the editor, we have provided the abstract *Book* class and a *Main* class. In the Main class, we created an instance of a class called *MyBook*. Your task is to write just the *MyBook* class. 


Your class mustn't be public.


**Sample Input**



```
A tale of two cities

```

**Sample Output**



```
The title is: A tale of two cities

```

## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Abstract Class](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-abstract-class/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-abstract-class/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-abstract-class/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-abstract-class/editorial) |

