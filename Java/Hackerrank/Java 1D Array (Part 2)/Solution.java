import java.util.*;

public class Solution {

    // Determines if the game can be won given the leap and game array
    public static boolean canWin(int leap, int[] game) {
        // If the game array is null, return false (no game to play)
        if (game == null) {
            return false;
        }
        // Start recursive exploration from position 0
        return isSolvable(leap, game, 0);
    }

    // Helper method that recursively checks if it's possible to solve the game from position i
    private static boolean isSolvable(int leap, int[] game, int i) {
        // Base Case: If i is beyond or exactly at the last index, you win the game
        if (i >= game.length) {
            return true;
        }
        // Base Case: If i is out of bounds or on a position that has already been visited or is blocked, return false
        else if (i < 0 || game[i] == 1) {
            return false;
        }

        // Mark the current position as visited by setting it to 1
        game[i] = 1;

        // Recursive Cases: Try to solve the game by:
        // 1. Moving forward by 'leap' positions
        // 2. Moving forward by 1 position
        // 3. Moving backward by 1 position
        return isSolvable(leap, game, i + leap)   // Leap forward
                || isSolvable(leap, game, i + 1)     // Step forward
                || isSolvable(leap, game, i - 1);    // Step backward
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // Read the number of test cases
        int q = scan.nextInt();

        // Process each test case
        while (q-- > 0) {
            int n = scan.nextInt();      // Size of the game array
            int leap = scan.nextInt();   // Leap value

            // Initialize and populate the game array
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            // Print "YES" if you can win the game, otherwise "NO"
            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }

        scan.close();
    }
}
