import java.io.*;
import java.util.*;
interface PerformOperation {
    boolean check(int a);
}
class MyMath {
    public static boolean checker(PerformOperation p, int num) {
        return p.check(num);
    }

    /**
     * Returns a lambda expression that checks if a number is odd.
     *
     * @return A PerformOperation that checks if a number is odd.
     */

    public static PerformOperation isOdd() {
        return n -> (n & 1) == 1;       // Use bitwise AND to check if the number is odd
    }

    /**
     * Returns a lambda expression that checks if a number is prime.
     *
     * @return A PerformOperation that checks if a number is prime.
     */

    public static PerformOperation isPrime() {
        return n -> {
            if (n < 2) {
                return false;       // Numbers less than 2 are not prime
            } else if (n == 2) {
                return true;        // 2 is the smallest prime number
            } else if (n % 2 == 0) {
                return false;       // Even numbers greater than 2 are not prime
            }
            int sqrt = (int) Math.sqrt(n);      // Check divisibility up to the square root of the number
            for (int i = 3; i <= sqrt; i += 2) {
                if (n % i == 0) {
                    return false;               // If divisible by any number, it's not prime
                }
            }
            return true;                    // If no divisors were found, it's prime
        };
    }

    /**
     * Returns a lambda expression that checks if a number is a palindrome.
     *
     * @return A PerformOperation that checks if a number is a palindrome.
     */

    public static PerformOperation isPalindrome() {
        return n -> {
            String original = Integer.toString(n);      // Convert the number to a string
            String reversed = new StringBuilder(Integer.toString(n)).reverse().toString();      // Reverse the string
            return original.equals(reversed);           // Check if the original and reversed strings are equal
        };
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        MyMath ob = new MyMath();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        PerformOperation op;
        boolean ret = false;
        String ans = null;
        while (T--> 0) {
            String s = br.readLine().trim();
            StringTokenizer st = new StringTokenizer(s);
            int ch = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            if (ch == 1) {
                op = ob.isOdd();
                ret = ob.checker(op, num);
                ans = (ret) ? "ODD" : "EVEN";
            } else if (ch == 2) {
                op = ob.isPrime();
                ret = ob.checker(op, num);
                ans = (ret) ? "PRIME" : "COMPOSITE";
            } else if (ch == 3) {
                op = ob.isPalindrome();
                ret = ob.checker(op, num);
                ans = (ret) ? "PALINDROME" : "NOT PALINDROME";

            }
            System.out.println(ans);
        }
    }
}
