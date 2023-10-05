# sum of n number
# xor of numbers


the for loop contains 2 lines the first is for xor all the numbers in the array the second is for xor all numbers from 1 to n (because ans originally contains zero we don't need to start from 0). For example if given array is [0 3 2] and 1 is missing the tracing of the program will be as follows :
start : ans=0
start the for loop:
i=0 ans=ans^nums[0]=0 ^0
ans=ans^(0+1)=0^0 ^1
i=1 ans=ans^nums[1]=0^0^1 ^3
ans=ans ^(1+1)=0^0^1^3 ^2
i=2 ans=ans^nums[2]=0^0^1^3^2 ^2
ans=ans^(2+1)=0^0^1^3^2^2 ^3
end of for loop

now you notice inside the ans var all numbers appeared twice except for 1 he missing number and there are two properties of xor :
1- any number xor itself is zero x ^ x=0
2- zero xor any number is the same number 0^ x=x
so all numbers that appear twice will cancel each other and we will end up with ans=0^1^0^0=1