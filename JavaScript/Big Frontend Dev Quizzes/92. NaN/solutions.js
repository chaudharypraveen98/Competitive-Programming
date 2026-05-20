// This is a JavaScript Quiz from BFE.dev 

console.log(NaN == NaN)
console.log(NaN === NaN)
console.log(Object.is(NaN, NaN))
console.log([NaN].indexOf(NaN))
console.log([NaN].includes(NaN))
console.log(Math.max(NaN, 1))
console.log(Math.min(NaN, 1))
console.log(Math.min(NaN, Infinity))

// false
// false
// true
// -1
// true
// NaN
// NaN
// NaN