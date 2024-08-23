import java.io.*;
import java.math.*;
import java.security.*;

import java.util.*;



public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        BigInteger n = scan.nextBigInteger();
        scan.close();
        System.out.println(n.isProbablePrime(10) ? "prime" : "not prime");
    }
}
