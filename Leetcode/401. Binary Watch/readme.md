Approach
1. Initialize an empty list to store the output.
2. Loop through all possible combinations of hours and minutes from 0 to 11 and 0 to 59 respectively.
3. For each combination, count the number of set bits in the binary representation of hours and minutes by using the count() method of the string representation of the binary number.
4. Check if the total number of set bits equals the input parameter turnedOn.
5. If it does, format the hours and minutes into a string with the required format of "HH:MM" and append it to the output list.
6. Return the output list.