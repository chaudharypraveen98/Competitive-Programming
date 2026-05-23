function* g() {
  console.log(1);
  try {
    console.log(2)
    yield 2
    console.log(3)
    throw new Error('error')
  } finally {
    console.log(4)
  }
}

const obj = g()
obj.next()
obj.return()

// 1
// 2
// 4