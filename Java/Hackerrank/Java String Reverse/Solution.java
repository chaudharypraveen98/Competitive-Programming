import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        // Create a Scanner object to read input
        Scanner sc = new Scanner(System.in);

        // Read the input string
        String A = sc.next();

        // Variable to track if the string is a palindrome
        boolean isPalindrome = true;

        // Length of the string
        int n = A.length();

        // Compare characters from the start and end
        for (int i = 0; i < n / 2; i++) {
            // If characters at opposite ends do not match
            if (A.charAt(i) != A.charAt(n - i - 1)) {
                isPalindrome = false; // Mark as not a palindrome
                break; // No need to continue checking
            }
        }

        // Output the result
        if (isPalindrome) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        // Close the scanner
        sc.close();
    }
}
