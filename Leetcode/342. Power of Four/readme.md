Approach:  
The binary representation of numbers with powers of four are the even powers of two
i.e
1 = 00000001
4 = 00000100
16 = 00010000
64 = 01000000

so the 1 arrives only at odd positions and there will only one 1 present in binary.

So to solve it
we will create a mask with binary literal mask = 0b01010101010101010101010101010101
32 bits with 1 at odd position

if we OR the mask with number and if the number is power of four then output will be the mask
i.e 16 OR mask = mask if 16 is power of four

but there is twist
if we have a number which has two 1's on odd positions such as number 20 = 00010100

in this case 20 OR mask will also be equal to mask cause the bits are on odd positions

To solve this problem we need to make sure that there is only one 1 present in the binary
to solve this (which is also the solution of another problem power of Two)

we subtract 1 from the number and do and operation
i.e
n = 100
n-1 = 011
if n & n-1 == 0 then we say that the number only has one 1 present in binary

finally we combine both of these things (masking and checking for single 1 bit)
we combine it produce the output