import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {

        // Import the Scanner class to handle input
        Scanner scan = new Scanner(System.in);

        // Read the size of the BitSets (N) and the number of operations to perform (M)
        int N = scan.nextInt();
        int M = scan.nextInt();

        // Initialize two BitSets of size N (all bits initialized to 0)
        BitSet B1 = new BitSet(N);
        BitSet B2 = new BitSet(N);

        // Perform M operations as specified
        while (M-- > 0) {
            // Read the operation command as a string
            String str = scan.next();

            // Read the two integer parameters a and b
            int a = scan.nextInt();
            int b = scan.nextInt();

            // Perform the operation based on the command
            switch (str) {
                case "AND":
                    // Perform the AND operation between the two BitSets
                    // If a == 1, perform B1 AND B2 (result is stored in B1)
                    // If a == 2, perform B2 AND B1 (result is stored in B2)
                    if (a == 1) {
                        B1.and(B2);
                    } else {
                        B2.and(B1);
                    }
                    break;
                case "OR":
                    // Perform the OR operation between the two BitSets
                    // If a == 1, perform B1 OR B2 (result is stored in B1)
                    // If a == 2, perform B2 OR B1 (result is stored in B2)
                    if (a == 1) {
                        B1.or(B2);
                    } else {
                        B2.or(B1);
                    }
                    break;
                case "XOR":
                    // Perform the XOR operation between the two BitSets
                    // If a == 1, perform B1 XOR B2 (result is stored in B1)
                    // If a == 2, perform B2 XOR B1 (result is stored in B2)
                    if (a == 1) {
                        B1.xor(B2);
                    } else {
                        B2.xor(B1);
                    }
                    break;
                case "FLIP":
                    // Flip the bit at index b in the respective BitSet
                    // If a == 1, flip the bit at index b in B1
                    // If a == 2, flip the bit at index b in B2
                    if (a == 1) {
                        B1.flip(b);
                    } else {
                        B2.flip(b);
                    }
                    break;
                case "SET":
                    // Set the bit at index b in the respective BitSet to 1
                    // If a == 1, set the bit at index b in B1
                    // If a == 2, set the bit at index b in B2
                    if (a == 1) {
                        B1.set(b);
                    } else {
                        B2.set(b);
                    }
                    break;
                default:
                    // If the operation is not recognized, do nothing
                    break;
            }

            // After each operation, print the number of set bits in both BitSets
            // B1.cardinality() returns the number of set bits in B1
            // B2.cardinality() returns the number of set bits in B2
            System.out.println(B1.cardinality() + " " + B2.cardinality());
        }

        scan.close();

    }
}