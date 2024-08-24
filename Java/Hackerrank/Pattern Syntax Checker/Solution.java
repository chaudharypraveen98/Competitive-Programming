import java.util.Scanner;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());

        // Loop through each test case
        while (testCases > 0) {
            String pattern = in.nextLine();

            try {
                // Attempt to compile the pattern using the Pattern.compile method
                Pattern.compile(pattern);
                // If compilation is successful, print "Valid"
                System.out.println("Valid");
            } catch (PatternSyntaxException e) {
                // If a PatternSyntaxException is caught, the pattern is invalid
                System.out.println("Invalid");
            }

            // Decrement the number of test cases
            testCases--;
        }

        // Close the scanner
        in.close();
    }
}
