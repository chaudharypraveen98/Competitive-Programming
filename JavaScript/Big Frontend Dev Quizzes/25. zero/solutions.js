// This is a JavaScript Quiz from BFE.dev

console.log(1 / 0)
console.log(-1 / 0)
console.log(0 / 0)
console.log(0 === -0)
console.log(Object.is(0, -0))
console.log(Object.is(0, Math.round(-0.5)))
console.log(Object.is(0, Math.round(0.5)))
console.log(0 * Infinity)
console.log(Infinity / Infinity)
console.log(Object.is(0, Math.sign(0)))
console.log(Object.is(0, Math.sign(-0)))
console.log(1 / -0)
console.log(1 / 0)
console.log(1n / 0n)


// Infinity
// -Infinity
// NaN
// true
// false
// false
// false
// NaN
// NaN
// true
// false
// -Infinity
// Infinity
// Error