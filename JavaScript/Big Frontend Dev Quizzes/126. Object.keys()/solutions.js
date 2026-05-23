console.log([
  ...Object.keys({a: 1, b: 2}),
  ...Object.keys({b: 2, a: 1})
])

// ["a","b","b","a"]