const a = {
  dev: 'BFE.dev',
  update: name => {
    this.dev = name
  }
}
a.update('bigfrontend.dev')
console.log(a.dev)

// "BFE.dev"