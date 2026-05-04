// This is a JavaScript Quiz from BFE.dev


console.log(0 == false) // 0==0 (boolean converted to number)
console.log('' == false) // ""==0 -> 0==0
console.log([] == false) // [] == 0 -> "" == 0 -> 0==0
console.log(undefined == false) // false (only undefined & null are equal in loose checking)
console.log(null == false) // false
console.log('1' == true) // '1' == 1 -> 1==1
console.log(1n == true) // 1n== 1 -> 1 == 1(Big int is number)
console.log(' 1     ' == true) //' 1     ' == 1 -> (toNumber is called on string, string is trimmed then converted)

// true
// true
// true
// false
// false
// true
// true
// true