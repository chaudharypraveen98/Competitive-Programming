// This is a JavaScript Quiz from BFE.dev

console.log([] + [])
console.log([] + 1)
console.log([[]] + 1)
console.log([[1]] + 1)
console.log([[[[2]]]] + 1)
console.log([] - 1)
console.log([[]] - 1)
console.log([[1]] - 1)
console.log([[[[2]]]] - 1)
console.log([] + {})
console.log({} + {})
console.log({} - {}) // NaN - NaN always results in NaN


// ""
// "1"
// "1"
// "11"
// "21"
// -1
// -1
// 0
// 1
// "[object Object]"
// "[object Object][object Object]"
// NaN