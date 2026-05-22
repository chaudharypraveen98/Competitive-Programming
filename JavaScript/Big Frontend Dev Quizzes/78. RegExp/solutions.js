// This is a JavaScript Quiz from BFE.dev 

const arr = ['a', 'b', 'c', '1']
const regExp = /^[a-z]$/gi
const chars = arr.filter(elem => regExp.test(elem))
console.log(chars)

// ["a","c"]