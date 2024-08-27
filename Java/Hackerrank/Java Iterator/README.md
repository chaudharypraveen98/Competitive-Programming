## [Java Iterator](https://www.hackerrank.com/challenges/java-iterator)

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![HackerRank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

| Difficulty | Max Score | Success Ratio |
|:-----------|:------------:|------------:|
| Easy       | 15      | 98.08%        |

Java Iterator class can help you to iterate through every element in a collection. Here is a simple example:



```
import java.util.*;
public class Example{

    public static void main(String []args){
        ArrayList mylist = new ArrayList();
        mylist.add("Hello");
        mylist.add("Java");
        mylist.add("4");
        Iterator it = mylist.iterator();
        while(it.hasNext()){
            Object element = it.next();
            System.out.println((String)element);
        }
    }
}

```

In this problem you need to complete a method *func*. The method takes an *ArrayList* as input. In that *ArrayList* there is one or more integer numbers, then there is a special string "\#\#\#", after that there are one or more other strings. A sample *ArrayList* may look like this:



```
element[0]=>42
element[1]=>10
element[2]=>"###"
element[3]=>"Hello"
element[4]=>"Java"

```

You have to modify the *func* method by editing `at most 2 lines` so that the code only prints the elements after the special string "\#\#\#". For the sample above the output will be:



```
Hello
Java

```

*Note:* The stdin doesn't contain the string *"\#\#\#"*, it is added in the *main* method. 


To restore the original code in the editor, click the top left icon on the editor and create a new buffer.


## 💡 Hints 

## ➡️ Approach 

## ✅ Detailed Solution
[View Solution : Java Iterator](./Solution.java)

| Submissions | Leaderboard| Discussions | Editorial |
|:-----------|:------------:|------------:|------------:|
| [📝 My Submission](https://www.hackerrank.com/challenges/java-iterator/submissions) | [🏆 Track our position](https://www.hackerrank.com/challenges/java-iterator/leaderboard) | [🤔 Help from Community](https://www.hackerrank.com/challenges/java-iterator/forum) | [✍️ Editorial](https://www.hackerrank.com/challenges/java-iterator/editorial) |

