/**
 * @param {Array} iterable
 * @return {Promise}
 */
export default function promiseAny(iterable) {
  if (iterable.length === 0) {
    return Promise.reject(new AggregateError([], "All promises were rejected"));
  }

  return new Promise((resolve, reject) => {
    let results = [];
    let completed = 0;
    iterable.forEach((promise, index) => {
      Promise.resolve(promise)
        .then((val) => {
          return resolve(val);
        })
        .catch((error) => {
          completed++;
          results[index] = error;
          if (completed === iterable.length) {
            return reject(new AggregateError(results, "Error"));
          }
        });
    });
  });
}
