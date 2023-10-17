Approach

1
---
Simple use hashmap/set to store and check and return

2
----
Explanation:
============

Hello there! Thanks for posting the solution. For any of you who are still confused allow me to explain:

Part1:  
unordered\_map<char, int> n2d{{'A', 0}, {'C', 1}, {'G', 2}, {'T', 3}};  
unordered\_set candidates;  
// this set should be much smaller than the candidates set. So using string should be ok.  
// You can also use integer if you want to.  
unordered\_set duplicates;

We have to represent 4 nucleotide. Simply put we have to represent 4 letters A, C, G, T. We know that 2 bits form 4 unique combinations. We can use these combinations to represent these 4 letter.

00 ->A  
01 ->C  
10 ->G  
11 ->T

So we are using 2 bits to represent a letter.

A 10 letter sequence will require -> 2x10=20 bits  
Size of integer -> 32 bits so we can easily store a 10 letter sequence in 20 bits.

How do we represent a 10 letter sequence?
=========================================

Say we have to represent ACGT using the 2 bit method we discussed above. So we will store as follows:

ans=0  
Adding A: ans=ans_4+A -> ans=0_4+0 ->ans=0 (binary rep of Ans:0)  
Adding C: ans=ans_4+C -> ans=0_4+1 ->ans=1(binary rep of Ans:1)  
Adding G: ans=ans_4+G->ans=1_4+2 ->ans=6(binary rep of Ans:110)  
Adding T: ans=ans_4+T-> ans=6_4+3 ->ans=27(binary rep of Ans:11011)

I am sure none of this makes any sense to you. That' okay lets consider it from the perspective of binary arithmetic.

As we said each letter requires 2 bits. So a letter sequence is nothing but a bit sequence. The sequence ACGT can be rep as :

                                   A       C       G       T
                                   |         |         |       |
                                 00       01      10    11

That means ACGT according to our 2 bit method can be represented as 000101011.

Note that this is the exact ans we have obtained above while calculating ans. This means that code is calculating this binary rep for the 10 letter sequence.

But why multiply by 4?
======================

Remember that multiplying a binary number 2 shifts it left by once as shown below:

                     1110 x 2 -> 11100 <- additional zero got added. Shifted to left.

So multiplying a number by 4 shifts it left twice (as 4=2x2 so we can think of multiplication by 4 as multiplication by 2 two times)

That means every time we multiply our result by 4 we introduce two 00 in rightmost positions.  
We do this because this is where bits of our current letter will go.

Example: let current ans be 0110  
So if we want to add the 2 bits representing the next letter we want to make space for them on the right. So we do it as follows:

(assuming the next letter to be added is C)

Making space for the bits of next letter: 0110 \* 4= 0110 00  
Adding the next letter: 0110 00 + C -> 0110 00 + 01 -> 0110 01

Notice how the bits 01 rep C got added to the new position that we created.

Why divide by (1<<18)?
======================

We know that our ans should at any given time only hold the binary rep of the last 10 letters. But we will add the binary rep of the current letter in the next step. That will make the ans to hold the binary rep of 11 letters but we don't want that. So we only hold binary rep of 9 letters at given time, because we know that in the next step we are going to add the binary rep of 1 more letter and hence making the total to be 10.

Each letter requires: 2bits  
9 letters require: 9x2=18bits

So to prevent anything in excess of binary rep of 18 bits just take ans mod (1<<18).

We do ans mod (1<<18) and not ans (mod 18) cause we are performing decimal arithmetic here. Hence we divide ans by decimal rep of 18 bits which is 1<<18

But why find ans for each 10 letter sequence?
=============================================

We represent a 10 letter sequence by a unique decimal number.  
That is, each 10 letter sequence will have its own unique decimal number and so we can store and use that number to identify whether a sequence occurs twice or more.

This is preferable since numbers are cheaper (computational wise) than Strings.