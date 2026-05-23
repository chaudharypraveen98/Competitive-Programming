const prettify = (str) => {
  try {
    if (typeof str === 'string') {
      JSON.parse(str)
      return "prettified"
    }
  } catch (e) {
    return "errored"
  } finally {
    return str
  }
}

console.log(prettify('BFE.dev'))
console.log(prettify('123'))

// "BFE.dev"
// "123"