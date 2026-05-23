function block(duration = 1000) {
  const start = Date.now()
  while (Date.now() - start < duration) {
    window.timestamp = Date.now()
  }
}

function a() {
   console.log(1)
   block()
   setTimeout(() => console.log(2), 0)
   setTimeout(() => console.log(3), 1)

}

function b() {
  console.log(4)
}

console.log(5)
setTimeout(a, 0)
setTimeout(b, 500)

// 5
// 1
// 2
// 4
// 3