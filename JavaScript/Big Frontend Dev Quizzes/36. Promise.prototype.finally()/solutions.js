// This is a JavaScript Quiz from BFE.dev

Promise.resolve(1)
.finally((data) => {
  console.log(data)
  return Promise.reject('error')
})
.catch((error) => {
  console.log(error)
  throw 'error2'
})
.finally((data) => {
  console.log(data)
  return Promise.resolve(2).then(console.log)
})
.then(console.log)
.catch(console.log)


// undefined
// "error"
// undefined
// 2
// "error2"