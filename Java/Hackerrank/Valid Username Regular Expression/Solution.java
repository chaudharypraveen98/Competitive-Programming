import java.util.Scanner;
class UsernameValidator {

    // - This regular expression ensures that the username:
    // - Starts with an alphabetic character [a-zA-Z].
    // - Is followed by alphanumeric characters or underscores [a-zA-Z0-9_].
    // - The total length of the username is between 8 and 30 characters.
    // - indicates the start of the string and $ indicates the end, ensuring the whole string follows the pattern.

    public static final String regularExpression = "^[a-zA-Z][a-zA-Z0-9_]{7,29}$";

}


public class Solution {
    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
    }
}