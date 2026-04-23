// This is a JavaScript coding problem from BFE.dev

/**
 * @param {any[]} arr
 * @returns {void}
 */
function shuffle(arr) {
    // generates negative and positives
    arr.sort(()=>Math.random())-0.5
}
// This solution is never considered because it is baised, Sorting algorithms (like Timsort in Chrome) are designed with the assumption that if $A > B$ and $B > C$, then $A$ must be $> C$ (transitivity). By using a random number, you break this rule. 
const arr = [1, 2, 3, 4];
shuffle(arr);
console.log("final", arr);

