const str = "BFE👍"
console.log(str.length)
console.log(str.slice(3, 4) == '👍')
console.log([...str].length)
console.log([...str].slice(3, 4) == '👍')

// 5
// false
// 4
// true