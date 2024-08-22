import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // Create a Scanner object to read input
        Scanner in = new Scanner(System.in);

        // Read the input string
        String S = in.next();

        // Read the start and end indices
        int start = in.nextInt();
        int end = in.nextInt();

        // Extract and print the substring from start to end (exclusive)
        System.out.println(S.substring(start, end));

        // Close the scanner
        in.close();
    }
}
