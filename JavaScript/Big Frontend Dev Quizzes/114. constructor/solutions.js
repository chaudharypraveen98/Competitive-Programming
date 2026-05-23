function A() {
  this.dev1 = 'BFE'
  this.dev2 = 'dev'
  return {
    dev1: 'bigfrontend'
  }
}

const a = new A()
console.log(a.dev1)
console.log(a.dev2)

// "bigfrontend"
// undefined