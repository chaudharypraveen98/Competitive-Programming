// This is a JavaScript Quiz from BFE.dev

function F() {
  this.foo = 'bar'
}

const f = new F()
console.log(f.prototype)

// undefined