/**
 * @param {any} thisArg
 * @param {...*} argArray
 * @return {any}
 */
Function.prototype.myCall = function (thisArg, ...argArray) {
    const context = thisArg === null || thisArg === undefined ? globalThis: Object(thisArg)
    const funcKey = Symbol('func');
    context[funcKey] = this;
    const res = context[funcKey](...argArray)
    delete context[funcKey];
    return res
};
function multiplyAge(multiplier = 1) {
  return this.age * multiplier;
}

const mary = {
  age: 21,
};

const john = {
  age: 42,
};

console.log(multiplyAge.myCall(mary)); // 21
console.log(multiplyAge.myCall(john, 2)); // 84