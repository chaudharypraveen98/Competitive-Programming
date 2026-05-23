class A {
  static dev = 'BFE'
  dev = 'bigfrontend'
}

class B extends A {
  log() {
    console.log(this.dev)
  }

  static log() {
    console.log(this.dev)
  }
}

B.log()
new B().log()


// "BFE"
// "bigfrontend"