function* gen() {
  try {
    yield 1
    yield 2
    return 3
    yield 4
  } finally {
    yield 5
    return 6
    yield 7
  }
}

console.log([...gen()])

// [1,2,5]