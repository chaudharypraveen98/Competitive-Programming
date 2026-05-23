function* genA() {
  yield [1, 2, 3]
}

function* genB() {
  yield* [1, 2, 3]
}

console.log(genA().next().value)
console.log(genB().next().value)

// [1,2,3]
// 1