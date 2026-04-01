/**
 * @param {Function} func
 * @return {Function}
 */
export default function curry(func) {
  return function curried(...args){
    if(args.length >= func.length){
        return func.apply(this, args)
    } else{
        return function(...next){
            return curried(...args, ...next)
        }.bind(this);
    }
  }
}

function multiplyThreeNumbers(a, b, c) {
  return a * b * c;
}

const curriedMultiplyThreeNumbers = curry(multiplyThreeNumbers);
console.log(curriedMultiplyThreeNumbers(4)(5)(6)); // 120

const containsFour = curriedMultiplyThreeNumbers(4);
const containsFourMulFive = containsFour(5);
console.log(containsFourMulFive(6)); // 120
