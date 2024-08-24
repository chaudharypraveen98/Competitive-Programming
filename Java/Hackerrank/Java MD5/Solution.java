import java.util.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Solution {

    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner scan = new Scanner(System.in);
        MessageDigest md = MessageDigest.getInstance("MD5");        // Get an instance of the MD5 MessageDigest object for computing MD5 hash
        md.update(scan.next().getBytes());                          // Read the next input string, convert it to bytes, and update the MessageDigest with it
        scan.close();

        byte[] digest = md.digest();            // Compute the hash (digest) of the input string

        // Convert the digest (byte array) into a hexadecimal string and print it
        // %02x ensures that each byte is formatted as a two-digit hexadecimal number

        for (byte b : digest) {
            System.out.format("%02x", b);
        }
    }
}