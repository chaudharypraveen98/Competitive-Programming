import java.util.Scanner;


public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int size = scan.nextInt();

        int[] array = new int[size];

        // Fill the array with input values
        for (int i = 0; i < size; i++) {
            array[i] = scan.nextInt();
        }
        scan.close();

        // Print the count of subarrays with negative sums
        System.out.println(negativeSubarrays(array));
    }

    // Method to count the number of subarrays with a negative sum
    private static int negativeSubarrays(int[] array) {
        int count = 0; // Variable to keep track of the number of negative subarrays

        // Iterate through all possible starting points of subarrays
        for (int i = 0; i < array.length; i++) {
            int sum = 0; // Initialize sum for the current subarray

            // Extend the subarray from index i to the end of the array
            for (int j = i; j < array.length; j++) {
                sum += array[j]; // Add the current element to the subarray sum

                // If the sum is negative, increment the count
                if (sum < 0) {
                    count++;
                }
            }
        }
        return count; // Return the total count of negative subarrays
    }
}
