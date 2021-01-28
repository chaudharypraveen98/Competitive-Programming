## **[Java Iterator](https://www.hackerrank.com/challenges/java-iterator)** 
Java Iterator class can help you to iterate through every element in a collection. Here is a simple example:<br><code>import java.util.*;
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
    }</code><br><br>You have to modify the <em>func</em> method by editing <code>at most 2 lines</code> so that the code only prints the elements after the special string "###". For the sample above the output will be:<br><br><br>