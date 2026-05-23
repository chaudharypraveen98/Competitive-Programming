const symbol = Symbol('BFE')

const a = {
  [symbol]: 'BFE',
  BFE: 'BFE'
}

console.log(symbol in a)
console.log('BFE' in a)
console.log(Object.keys(a).length)

// true
// true
// 1