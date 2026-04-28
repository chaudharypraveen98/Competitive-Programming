// This is a JavaScript Quiz from BFE.dev

for (var i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 0)
}
// var has a global scope, async is executed at later task and variable already reached last one
// 5
// 5
// 5
// 5
// 5

for (let i = 0; i < 5; i++) {
  setTimeout(() => console.log(i), 0)
}

// 0
// 1
// 2
// 3
// 4