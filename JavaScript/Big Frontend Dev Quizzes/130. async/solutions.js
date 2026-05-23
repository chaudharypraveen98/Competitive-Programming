const promise = Promise.resolve()
function f() {
  return promise
}

async function a() { return f() }
async function b() { return await f() }
function c() { return f() }

console.log(a() === b())
console.log(b() === c())
console.log(a() === c())

// false
// false
// false