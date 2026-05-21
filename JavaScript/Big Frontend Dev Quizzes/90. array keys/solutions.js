// This is a JavaScript Quiz from BFE.dev 

console.log(Reflect.ownKeys([]))
console.log(Reflect.ownKeys([,]))
console.log(Reflect.ownKeys([1,,2]))
console.log(Reflect.ownKeys([...[1,,2]]))

// ["length"]
// ["length"]
// ["0","2","length"]
// ["0","1","2","length"]