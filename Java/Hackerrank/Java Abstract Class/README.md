## **[Java Abstract Class](https://www.hackerrank.com/challenges/java-abstract-class)** 
A Java abstract class is a class that can't be instantiated. That means you cannot create new instances of an abstract class. It works as a base for subclasses. You should learn about Java Inheritance before attempting this challenge.<br>Following is an example of abstract class:<br><code>abstract class Book{
    String title;
    abstract void setTitle(String s);
    String getTitle(){
        return title;
    }
}</code><br>If you try to create an instance of this class like the following line you will get an error:<br><code></code><br><br><br><br><br><br><br>