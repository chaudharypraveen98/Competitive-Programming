import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // Initialize a 6x6 2D array
        int arr[][] = new int[6][6];

        // Loop through each element in the 2D array to fill it with input values
        for (int row = 0; row < 6; row++) {
            for (int col = 0; col < 6; col++) {
                arr[row][col] = scan.nextInt();
            }
        }
        scan.close();

        // Print the maximum hourglass sum from the array
        System.out.println(maxHourglass(arr));
    }

    // Method to find the maximum hourglass sum
    public static int maxHourglass(int [][] arr) {
        int max = Integer.MIN_VALUE; // Initialize max to the smallest possible integer value

        // Loop through all possible hourglass top-left corners (rows 0-3 and columns 0-3)
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 4; col++) {
                // Calculate the sum of the current hourglass
                int sum = findSum(arr, row, col);

                // Update the maximum sum if the current hourglass sum is larger
                max = Math.max(max, sum);
            }
        }
        return max; // Return the maximum hourglass sum found
    }

    // Helper method to calculate the sum of an hourglass pattern starting at (r, c)
    private static int findSum(int [][] arr, int r, int c) {
        // Calculate the sum of the hourglass shape
        int sum = arr[r+0][c+0] + arr[r+0][c+1] + arr[r+0][c+2] // Top 3 elements of the hourglass
                + arr[r+1][c+1] +               // Middle element of the hourglass
                arr[r+2][c+0] + arr[r+2][c+1] + arr[r+2][c+2]; // Bottom 3 elements of the hourglass
        return sum; // Return the hourglass sum
    }
}
