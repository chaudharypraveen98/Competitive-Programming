// This is a JavaScript Quiz from BFE.dev

console.log(1)
const promise = new Promise((resolve) => {
  // sync task inside declaration will print
  console.log(2)
  resolve()
  console.log(3)
})

console.log(4)

promise.then(() => {
    // promises are micro task will be picked before
    console.log(5);
}).then(() => {
  console.log(6)
})

console.log(7)

setTimeout(() => {
  console.log(8)
}, 10)

setTimeout(() => {
  console.log(9)
}, 0)

// 1
// 2
// 3
// 4
// 7
// 5
// 6
// 9
// 8