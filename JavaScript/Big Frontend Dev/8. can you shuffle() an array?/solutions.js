// This is a JavaScript coding problem from BFE.dev

/**
 * @param {any[]} arr
 * @returns {void}
 */
function shuffle(arr) {
    const res = [];
    while (arr.length) {
        const randomIndex = Math.floor(Math.random() * arr.length);
        const [item] = arr.splice(randomIndex, 1);
        res.push(item);
    }
    for (let i = 0; i < res.length; i++) {
        arr[i] = res[i];
    }
}

const arr = [1, 2, 3, 4];
shuffle(arr);
console.log("final", arr);
