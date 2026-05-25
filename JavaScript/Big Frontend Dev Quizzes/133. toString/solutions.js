const obj = {}
const fun = () => {}
console.log(obj.toString === Object.toString)
console.log(fun.toString === Function.toString)
console.log(obj.toString === Object.prototype.toString)
console.log(fun.toString === Function.prototype.toString)
console.log(Object.toString === Object.prototype.toString)
console.log(Function.toString === Function.prototype.toString)

// false
// true
// true
// true
// false
// true