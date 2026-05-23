function* gen() {
  yield 1 
  try {
    yield 2
    yield 3
  } finally {
    yield 4
  }
  yield 5
}

const g = gen()
console.log(g.next().value)
console.log(g.next().value)
console.log(g.return(6).value)
console.log(g.next().value)
console.log(g.next().value)

// 1
// 2
// 4
// 6
// undefined