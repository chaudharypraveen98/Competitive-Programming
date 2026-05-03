// This is a JavaScript Quiz from BFE.dev

let a = 1
const b = ++a // symbol is first then value is updated then returned
const c = a++ // value is returned first then updated as side effect
console.log(a)
console.log(b)
console.log(c)

// 3
// 2
// 2