/**
 * @param {Array<(arg: any) => any>} funcs
 * @return {(arg: any) => any}
 */
function pipe(funcs) {
    return (x)=>funcs.reduce((acc, f)=>f(acc),x)
}

const times = (y) => (x) => x * y;
const plus = (y) => (x) => x + y;
const subtract = (y) => (x) => x - y;
const divide = (y) => (x) => x / y;

console.log(pipe([times(2), times(3)])(5));
// x * 2 * 3
console.log(pipe([times(2), plus(3), times(4)])(1));
// (x * 2 + 3) * 4
console.log(pipe([times(2), subtract(3), divide(4)])(2));
// (x * 2 - 3) / 4
