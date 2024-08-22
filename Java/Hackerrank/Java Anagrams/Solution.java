import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // If the lengths are not equal, the strings can't be anagrams
        if (a.length() != b.length())
            return false;

        // Convert both strings to lowercase to ensure case insensitivity
        a = a.toLowerCase();
        b = b.toLowerCase();

        // Create two arrays to count the occurrences of each character (assuming only lowercase letters)
        int[] charCountA = new int[26];  // For string 'a'
        int[] charCountB = new int[26];  // For string 'b'

        // Count the occurrences of each character in string 'a' and 'b'
        for (int i = 0; i < a.length(); i++) {
            charCountA[a.charAt(i) - 'a']++;  // Increment the count for character in 'a'
            charCountB[b.charAt(i) - 'a']++;  // Increment the count for character in 'b'
        }

        // Compare the two frequency arrays
        for (int i = 0; i < 26; i++) {
            // If any character has a different count in 'a' and 'b', they are not anagrams
            if (charCountA[i] != charCountB[i]) {
                return false;
            }
        }

        // If all character counts match, the strings are anagrams
        return true;
    }


    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}