import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DuplicateWords {

    public static void main(String[] args) {

        // Define a regular expression to find duplicate words in a sentence
        // \b(\\w+) - Matches a word boundary followed by one or more word characters (a word)
        // (\\W+\\1\\b)+ - Matches one or more non-word characters followed by the previously matched word, ensuring it's a duplicate

        String regex = "\\b(\\w+)(\\W+\\1\\b)+";

        // Compile the regex pattern with case insensitivity to handle duplicate words regardless of case

        Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);

        Scanner in = new Scanner(System.in);
        int numSentences = Integer.parseInt(in.nextLine());

        // Process each sentence

        while (numSentences-- > 0) {
            String input = in.nextLine();

            // Create a matcher that will find occurrences of the pattern in the input sentence

            Matcher m = p.matcher(input);

            // Find all subsequences in the input that match the compiled regex pattern
            while (m.find()) {

                // Replace the entire matched subsequence with the first occurrence of the word (m.group(1))
                // This effectively removes the duplicate words

                input = input.replaceAll(m.group(), m.group(1));

            }

            // Print the modified sentence, with duplicates removed
            System.out.println(input);
        }
        in.close();
    }
}