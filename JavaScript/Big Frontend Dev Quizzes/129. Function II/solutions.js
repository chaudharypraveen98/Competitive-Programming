console.log(Function.prototype.__proto__ === Object.prototype)
console.log(Function.__proto__ === Object.__proto__)
console.log(Function.__proto__.__proto__ === Object.prototype)
console.log(Object.constructor.prototype === Object.prototype)
console.log(Function.constructor === Function)
console.log(Object.constructor === Object)
console.log(Array.__proto__ === Function.__proto__)
console.log(Array.constructor === Function)
console.log(Object.__proto__ === Function)
console.log(Function.__proto__ === Function.prototype)
console.log(Object instanceof Object)
console.log(Function instanceof Function)
console.log(Map instanceof Map)

// true
// true
// true
// false
// true
// false
// true
// true
// false
// true
// true
// true
// false