## **[Java Stdin and Stdout I](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1)** 
Most HackerRank challenges require you to read input from stdin (standard input) and write output to stdout (standard output).<br>One popular way to read input from stdin is by using the Scanner class and specifying the Input Stream as System.in. For example:<br><code>Scanner scanner = new Scanner(System.in);
String myString = scanner.next();
int myInt = scanner.nextInt();
scanner.close();

System.out.println("myString is: " + myString);
System.out.println("myInt is: " + myInt);</code><br>The code above creates a Scanner object named and uses it to read a String and an int. It then closes the Scanner object because there is no more input to read, and prints to stdout using . So, if our input is:<br><br><br><br><br>**Sample Input 0**<br><br>**Sample Output 0**<br><br>