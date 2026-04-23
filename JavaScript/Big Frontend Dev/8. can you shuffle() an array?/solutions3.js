// This is a JavaScript coding problem from BFE.dev

/**
 * @param {any[]} arr
 * @returns {void}
 */
function shuffle(arr) {
    let i =  arr.length-1;
    while (i>0) {
        const j = Math.floor(Math.random() * (i+1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
        i--;
    }
}

const arr = [1, 2, 3, 4];
shuffle(arr);
console.log("final", arr);
