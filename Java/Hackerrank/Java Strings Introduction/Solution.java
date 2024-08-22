import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        // Create a Scanner object for reading input
        Scanner sc = new Scanner(System.in);

        // Read the two input strings A and B
        String A = sc.next();
        String B = sc.next();

        // 1. Print the sum of lengths of A and B
        int totalLength = A.length() + B.length();
        System.out.println(totalLength);

        // 2. Determine if A is lexicographically greater than B
        if (A.compareTo(B) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        // 3. Capitalize the first letter of A and B and print them
        String capitalizedA = A.substring(0, 1).toUpperCase() + A.substring(1);
        String capitalizedB = B.substring(0, 1).toUpperCase() + B.substring(1);
        System.out.println(capitalizedA + " " + capitalizedB);

        // Close the scanner
        sc.close();
    }
}
