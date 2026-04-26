// This is a JavaScript Quiz from BFE.dev

Promise.resolve(1)
.then(() => 2)
.then(3)
.then((value) => value * 3)
.then(Promise.resolve(4))
.then(console.log)


/**
 * CORE CONCEPT: Promise Fallthrough
 * * As part of Asynchronous Orchestration, understanding how .then() handles arguments 
 * is vital for avoiding architectural "leaks."
 * * EXECUTION BREAKDOWN:
 * 1. Promise.resolve(1)        -> Initial resolved value: 1.
 * 2. .then(() => 2)            -> Function returns 2; new resolved value is 2.
 * 3. .then(3)                  -> FALLTHROUGH: '3' is not a function. The previous 
 * value 2 passes through.
 * 4. .then((v) => v * 3)       -> Function executes 2 * 3 = 6.
 * 5. .then(Promise.resolve(4)) -> FALLTHROUGH: A Promise object is NOT a function. 
 * The previous value 6 passes through.
 * 6. .then(console.log)        -> Receives and logs the final value: 6.
 * * THE "WHY": 
 * Promise.prototype.then() strictly expects a function as its argument. If a 
 * non-function (number, string, or even a Promise object) is provided, it is 
 * treated as null. This triggers "fallthrough," where the chain ignores that 
 * step and passes the last successfully resolved value to the next handler.
 */
// 6