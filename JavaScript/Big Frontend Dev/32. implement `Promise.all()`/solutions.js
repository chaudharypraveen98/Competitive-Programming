/**
 * @param {Array<any>} promises - notice input might have non-Promises
 * @return {Promise<any[]>}
 */
function all(promises) {
    if (promises.length === 0) {
        return Promise.resolve([]);
    }
    return new Promise((resolve, reject) => {
        let results = [];
        let resolvedCount = 0;

        promises.forEach((promise, index) => {
            return Promise.resolve(promise)
                .then((val) => {
                    results[index] = val;
                    resolvedCount++;
                    if (resolvedCount === promises.length) {
                        resolve(results);
                    }
                })
                .catch((error) => {
                    reject(error);
                });
        });
    });
}
