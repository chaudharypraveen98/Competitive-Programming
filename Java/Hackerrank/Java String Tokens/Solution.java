import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();

        // Split the string based on the given regex and remove any empty tokens
        String[] tokens = s.split("[ !,?._'@]+");

        // Create a list to store valid tokens (non-empty strings)
        List<String> validTokens = new ArrayList<>();

        for (String token : tokens) {
            if (!token.isEmpty()) {
                validTokens.add(token);
            }
        }

        // Print the number of valid tokens
        System.out.println(validTokens.size());

        // Print each valid token
        for (String token : validTokens) {
            System.out.println(token);
        }

        scan.close();
    }
}
