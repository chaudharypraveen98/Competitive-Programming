import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numLines = scanner.nextInt();
        scanner.nextLine();

        // Create a list to store lines of integers
        List<List<Integer>> listOfLines = new ArrayList<>();

        // Read each line
        for (int i = 0; i < numLines; i++) {
            // Read the line as a string and split by spaces
            String[] inputLine = scanner.nextLine().split(" ");
            // Create a list for this line of integers
            List<Integer> line = new ArrayList<>();
            // Read the integers into the list, skipping the first element (number of integers)
            for (int j = 1; j < inputLine.length; j++) {
                line.add(Integer.parseInt(inputLine[j]));
            }
            // Add this line to the list of lines
            listOfLines.add(line);
        }

        // Read number of queries
        int numQueries = scanner.nextInt();

        // Process each query
        for (int i = 0; i < numQueries; i++) {
            int lineIndex = scanner.nextInt() - 1; // Convert to zero-based index
            int positionIndex = scanner.nextInt() - 1; // Convert to zero-based index

            // Check if the line index is within bounds
            if (lineIndex >= 0 && lineIndex < listOfLines.size()) {
                List<Integer> line = listOfLines.get(lineIndex);
                // Check if the position index is within bounds
                if (positionIndex >= 0 && positionIndex < line.size()) {
                    System.out.println(line.get(positionIndex));
                } else {
                    System.out.println("ERROR!");
                }
            } else {
                System.out.println("ERROR!");
            }
        }

        scanner.close();
    }
}
