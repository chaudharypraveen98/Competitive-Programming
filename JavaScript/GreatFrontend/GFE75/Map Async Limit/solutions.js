/**
 * @param {Array<any>} iterable
 * @param {Function} callbackFn
 * @param {number} size
 *
 * @return {Promise}
 */
export default function mapAsyncLimit(iterable, callbackFn, size=iterable.length) {
    if (iterable.length === 0) {
        return Promise.resolve([]);
    }

    return new Promise((resolve, reject) => {
        let isRejected = false;
        let completed = 0;
        let results = [];
        let currentIndex = 0;

        function worker() {
            if (isRejected || currentIndex >= iterable.length) {
                return;
            }
            const index = currentIndex++;

            Promise.resolve(callbackFn(iterable[index]))
                .then((val) => {
                    if (isRejected) return;

                    completed++;
                    results[index] = val;

                    if (completed === iterable.length) {
                        resolve(results);
                    } else{
                        worker()
                    }
                })
                .catch((error) => {
                    isRejected = true;
                    reject(error);
                });
        }
        const initialWorkers = Math.min(iterable.length, size);
        for(let i=0; i < initialWorkers; i++) {
            worker();
        }
    });
}


async function fetchUpperCase(q) {
    // Fake API service that converts a string to uppercase.
    const res = await fetch("https://uppercase.com?q=" + encodeURIComponent(q));
    return await res.text();
}

// Only a maximum of 2 pending requests at any one time.
const results = await mapAsyncLimit(
    ["foo"],
    fetchUpperCase,
    2,
);
console.log(results); // ['FOO', 'BAR', 'QUX', 'QUZ'];
