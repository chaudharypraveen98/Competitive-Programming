import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {
    public static void main(String[] args) {
        Scanner scan  = new Scanner(System.in);

        // Read the number of test cases
        int testCases = Integer.parseInt(scan.nextLine());

        // Process each test case
        while (testCases-- > 0) {
            // Read the input line (which contains HTML-like tags)
            String line = scan.nextLine();
            boolean matchFound = false; // A flag to track if any matches were found

            // Define a regex pattern to match HTML tags and their contents
            // <(.+)> matches any opening HTML tag and captures the tag name (.+) inside the angle brackets
            // ([^<]+) captures the content between the opening and closing tags (i.e., the text between tags)
            // </\\1> matches the corresponding closing tag by referring to the first captured group (\\1)
            Pattern r = Pattern.compile("<(.+)>([^<]+)</\\1>");

            // Create a matcher to find matches of the regex pattern in the input line
            Matcher m = r.matcher(line);

            // Loop through all matches found in the line
            while (m.find()) {
                // Print the content between the HTML tags (captured by group 2)
                System.out.println(m.group(2));
                matchFound = true; // Set the flag to true since a match was found
            }

            // If no matches were found, print "None"
            if (!matchFound) {
                System.out.println("None");
            }
        }

        scan.close();
    }
}
