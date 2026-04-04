/**
 * @param {any} val
 * @param {Array<string>} keys
 * @returns any
 */

export default function deepOmit(val, keys) {
  let seen = new WeakMap()
  function deepCopy(obj ) {
    if (typeof obj !== "object" || obj===null) {
      return obj;
    }
    if (seen.has(obj)) {
      return seen.get(obj);
    }
    const isArray = Array.isArray(obj);
    let res = isArray ? [] : {};
    seen.set(obj, res);
    if (isArray) {
      for (const item of obj) {
        res.push(deepCopy(item));
      }
    } else {
      for (const objKey of Object.keys(obj)) {
        if (!keys.includes(objKey)) {
          res[objKey] = deepCopy(obj[objKey]);
        }
      }
    }
    return res;
  }
  return deepCopy(val);
}


const obj = {
  a: 1,
  b: 2,
  c: {
    d: 3,
    e: 4,
  },
  f: [5, 6],
};

console.log(deepOmit(obj, ["b", "c", "e"])); // { a: 1, f: [5, 6] }
