/**
 * @param {() => Promise<any>} func
 * @param {number} max
 * @return {Promise}
 */
function throttlePromises(funcs, max) {
    if (funcs.length === 0) {
        return Promise.resolve([]);
    }
    return new Promise((resolve, reject) => {
        let results = [];
        let currentIndex = 0;
        let isRejected = false;
        let completedTask = 0;
        console.log("inside");

        function workerNode() {
            if (isRejected || currentIndex >= funcs.length) {
                return;
            }
            const index = currentIndex++;
            const task = funcs[index];
            return Promise.resolve(task())
                .then((val) => {
                    if (isRejected) return;
                    results[index] = val;
                    completedTask++;
                    if (completedTask === funcs.length) {
                        resolve(results);
                    } else {
                        workerNode();
                    }
                })
                .catch((error) => {
                    isRejected = true;
                    reject(error);
                });
        }
        const initialWorkers = Math.min(funcs.length, max);
        Array.from({ length: initialWorkers }).forEach(() => workerNode());
    });
}
// Fixed Mock: Array of functions that return Promises
const callApis = [
    () => new Promise((res) => setTimeout(() => res(1), 1000)),
    () => new Promise((res) => setTimeout(() => res(2), 500)),
    () => new Promise((res) => setTimeout(() => res(3), 100)),
    () => new Promise((res) => setTimeout(() => res(1), 1000)),
    () => new Promise((res) => setTimeout(() => res(2), 500)),
    () => new Promise((res) => setTimeout(() => res(3), 100)),
];

throttlePromises(callApis, 2)
    .then((data) => console.log("Final Results:", data)) // [1, 2, 3]
    .catch((err) => console.log("err", err));
