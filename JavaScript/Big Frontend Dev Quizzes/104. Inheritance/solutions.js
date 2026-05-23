class A {
  a = 'a'
}

A.prototype.c = 'c'

class B extends A {
  b = 'b'
}

const a = new A()
const b = new B()

console.log(a.a)
console.log(a.b)
console.log(a.c)
console.log(b.a)
console.log(b.b)
console.log(b.c)

// "a"
// undefined
// "c"
// "a"
// "b"
// "c"