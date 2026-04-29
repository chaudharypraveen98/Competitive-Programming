// This is a JavaScript Quiz from BFE.dev

const obj = {
  dev: 'bfe',
  a: function() {
    return this.dev
  }, 
  b() {
    return this.dev
  }, //Both a and b are normal functions, When a function is called as a method of an object, it's this is set to the object the method is called on (i.e. obj object)
  c: () => {
    return this.dev
  }, // this is an arrow function, apply rule 6 in the above link and since there is no surrounding function here the this is by default window object and thus, answer is undefined.
  d: function() {
    return (() => {
      return this.dev
    })()
  }, // again, arrow function, answer is the surrounding function this. which is 'bfe'
  e: function() {
    return this.b()
  }, // here this.b() is being called and since, this is pointing to object's scope, it is 'bfe' only
  f: function() {
    return this.b
  }, // here function is being returned as it is and since we invoke the function in console.log statement it will point to default window scope, hence undefined
  g: function() {
    return this.c()
  }, // even after attaching this to the arrow function, it does not affects the underlying properties of the arrow function. hence, undefined
  h: function() {
    return this.c
  }, // here function is being returned as it is and since we invoke the function in console.log statement it will point to default window scope, hence undefined
  i: function() {
    return () => {
      return this.dev
    }
  } // this is a function closure and it will remember the scope of this which is pointing to object's scope only. Thus, answer is 'bfe'.
}


console.log(obj.a())
console.log(obj.b())
// console.log(obj.c())
console.log(obj.d())
console.log(obj.e())
console.log(obj.f()())
console.log(obj.g())
console.log(obj.h()())
console.log(obj.i()())

// "bfe"
// "bfe"
// undefined
// "bfe" 
// "bfe"
// undefined
// undefined
// undefined
// "bfe"