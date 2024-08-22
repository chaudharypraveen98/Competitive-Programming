import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        // Initialize the smallest and largest strings as the first substring of length k
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);

        // Iterate over all possible substrings of length k
        for (int i = 1; i <= s.length() - k; i++) {
            // Get the current substring of length k
            String substring = s.substring(i, i + k);

            // Compare and update smallest and largest if necessary
            if (substring.compareTo(smallest) < 0) {
                smallest = substring;
            }
            if (substring.compareTo(largest) > 0) {
                largest = substring;
            }
        }

        // Return the result in the required format
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}