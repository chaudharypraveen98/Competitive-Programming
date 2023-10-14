An efficient approach to solving this problem without using extra space is to use bitwise XOR. Here are the steps:

1. Initialize two variables, xor and mask, to 0. These will be used to store the XOR result of the two unique numbers and a bitmask to separate them.
Iterate through the given array.
2. For each element in the array, calculate the XOR of xor and the element and update xor.
3. Calculate the mask as the rightmost set bit in xor. This can be done by finding the rightmost 1-bit in xor and then creating a bitmask with only that bit set to 1.
Initialize two variables, result1 and result2, to 0. These will be used to store the two unique numbers.
Iterate through the array again.
4. For each element in the array, check if the mask bit is set. If it is, XOR it with result1; otherwise, XOR it with result2.
After the iteration, result1 and result2 will contain the two unique numbers.
Return an array containing result1 and result2.