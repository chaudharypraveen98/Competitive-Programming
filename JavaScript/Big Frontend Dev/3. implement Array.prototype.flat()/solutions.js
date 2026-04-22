// This is a JavaScript coding problem from BFE.dev
/**
 * @param { Array } arr
 * @param { number } depth
 * @returns { Array }
 */
function flat(arr, depth = 1) {
    if (depth === 0) {
        return arr;
    }
    let res = [];
    for (let i=0; i< arr.length;i++) {
        if(!(i in arr)) continue;
        const item = arr[i]
        if (Array.isArray(item)) {
            res = res.concat(flat(item, depth - 1));
        } else {
            res.push(item);
        }
    }
    return res;
}

const arr = [1, [2], [3, [4]]];
console.log(flat(arr));
[1, 2, 3, [4]];
console.log(flat(arr, 1));
// [1, 2, 3, [4]]
console.log(flat(arr, 2));
// [1, 2, 3, 4]

console.log(flat([1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]], Infinity));
