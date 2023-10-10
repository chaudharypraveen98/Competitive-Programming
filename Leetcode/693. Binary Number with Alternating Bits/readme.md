Approach
1. Check the consecutive bits, if same then return false else true
2. temp = (number>>1)+number. return (temp&temp+1)==0
   ```
   //      10101010101
    //  +    1010101010    ( number >> 1 )
    //  ---------------
    //  =   11111111111
    //  &  100000000000
    //  ---------------
    //  =             0    ( power of two )
    let tmp = ( number >> 1 ) + number;
    return (tmp & tmp + 1) === 0;```