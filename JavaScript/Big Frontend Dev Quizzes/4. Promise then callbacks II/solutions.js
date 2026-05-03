// This is a JavaScript Quiz from BFE.dev

Promise.resolve(1)
.then((val) => {
  console.log(val)
  return val + 1
}).then((val) => {
  console.log(val)
}).then((val) => {
  console.log(val)
  return Promise.resolve(3)
    .then((val) => {
      console.log(val)
    })
}).then((val) => {
  console.log(val)
  return Promise.reject(4)
}).catch((val) => {
  console.log(val)
}).finally((val) => {
    console.log(val); // return previous next value to handler
    return 10;
}).then((val) => {
  console.log(val)
})

/**
 * EXECUTION FLOW SUMMARY:
 * 1. Log 1: From initial Promise.resolve(1).
 * 2. Log 2: From the first .then(), which returns 1 + 1.
 * 3. Log undefined: From the second .then(), as the previous step returned nothing.
 * 4. Log 3: From the nested promise inside the third .then(). The outer chain waits for this to finish.
 * 5. Log undefined: From the result of the third .then() chain finishing.
 * 6. Log 4: From the .catch() block, which consumes the rejection from the previous step.
 * 7. Log undefined: The .catch() resolves successfully, passing undefined forward.
 * 8. Log undefined: The .finally() executes, ignoring its return value (10) 
 * and passing through the previous undefined to the final .then().
 */

// 1
// 2
// undefined
// 3
// undefined
// 4
// undefined
// undefined