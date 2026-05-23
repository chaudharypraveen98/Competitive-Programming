// This is a JavaScript Quiz from BFE.dev 

class Dev {
  #name
  constructor(name) {
    this.#name = name
  }
  get name() {
    return this.#name;
  }
}

const dev = new Dev('BFE')
console.log(dev.name)

const proxyDev = new Proxy(dev, {})
console.log(proxyDev.name)

// "BFE"
// Error