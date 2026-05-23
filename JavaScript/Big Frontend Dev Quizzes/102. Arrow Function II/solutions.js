class Site {
  name = 'BFE'
  getHandle() {
    return {
      name: 'bigfrontend',
      getName1() {
        return this.name
      },
      getName2: () => {
        return this.name
      },
      getName3: function() {
        return this.name
      }
    }
  }
}

const site = new Site()
console.log(site.getHandle().getName1())
console.log(site.getHandle().getName2())
console.log(site.getHandle().getName3())


// "bigfrontend"
// "BFE"
// "bigfrontend"