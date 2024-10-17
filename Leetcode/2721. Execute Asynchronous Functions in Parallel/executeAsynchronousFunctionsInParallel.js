/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function (functions) {
  return new Promise((resolve, reject) => {
    let arr = [];
    let resolved = 0;
    functions.forEach((fn, idx) => {
      fn()
        .then((res) => {
          arr[idx] = res;
          resolved++;
          if (functions.length == resolved) {
            resolve(arr);
          }
        })
        .catch((err) => {
          reject(err);
        });
    });
    if (functions.length === 0) {
      resolve(arr);
    }
  });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
