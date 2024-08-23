import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.HashMap;

public class test {
    public static void main(String[] args) {
        // HashMap to keep track of the frequency of integers in the current window
        HashMap<Integer, Integer> map = new HashMap<>();

        // ArrayDeque to represent the sliding window of size m
        ArrayDeque<Integer> deque = new ArrayDeque<>();


        Scanner scan = new Scanner(System.in);

        // Read the total number of integers (n) and the size of the subarray (m)
        int n = scan.nextInt();
        int m = scan.nextInt();

        // Variable to keep track of the maximum number of unique integers found
        int max = 0;

        // Loop through all the integers
        for (int i = 0; i < n; i++) {
            // If the sliding window has exceeded size m, remove the oldest element
            if (i >= m) {
                int old = deque.removeFirst();  // Remove the oldest element from the deque

                // Decrease the frequency of the removed element in the map
                if (map.get(old) == 1) {
                    // If the frequency is 1, remove it from the map
                    map.remove(old);
                } else {
                    // Otherwise, decrease the frequency by 1
                    map.merge(old, -1, Integer::sum);
                }
            }

            // Add the new number to the deque (sliding window)
            int num = scan.nextInt();
            deque.addLast(num);

            // Increase the frequency of the new number in the map
            map.merge(num, 1, Integer::sum);

            // Update the maximum number of unique integers
            max = Math.max(max, map.size());

            // If the maximum number of unique integers is equal to m, break early
            if (max == m) {
                break;
            }
        }

        scan.close();

        // Print the maximum number of unique integers found
        System.out.println(max);
    }
}
