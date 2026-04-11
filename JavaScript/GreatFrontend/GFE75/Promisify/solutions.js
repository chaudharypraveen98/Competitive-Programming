/**
 * @callback func
 * @returns Function
 */
export default function promisify(func) {
  return function(...args){
     return new Promise((resolve, reject)=>{
        func.call(this, ...args, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
     })
  }
}

// Example function with callback as last argument
// The callback has the signature `(err, value) => any`
function foo(url, options, callback) {
  apiCall(url, options)
    .then((data) => callback(null, data))
    .catch((err) => callback(err));
}

const promisifiedFoo = promisify(foo);
const data = await promisifiedFoo('example.com', { foo: 1 });
console.log(data)