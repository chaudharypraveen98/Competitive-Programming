## Approach
The main concept lies that ones*zeros  are the distance of each column
  
    a = 0 0 0 1 0
    b = 1 0 0 1 1
    c = 0 1 0 0 1
    d = 1 0 0 1 0
    e = 0 0 0 1 0
                ↑
    ones: b, c
    zeros: a, d, e
    
    pairs that make distance are:
    b: a, d, e
    c: a, d, e

    So we have 2 ones and 5 - 2 = 3 zeros
    Total distance = 2 * 3
    then we move the pointer one position left, i.e. all the numbers right shift by 1 (num >>> 1)