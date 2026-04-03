/**
 * @param {*} valueA
 * @param {*} valueB
 * @return {boolean}
 */
export default function deepEqual(valueA, valueB) {
  const typeValueA = typeof valueA;
  const typeValueB = typeof valueB;
  if (typeValueA !== typeValueB) {
    return false;
  }
  if (valueA === null) {
    return valueA === valueB;
  }

  if (
    typeValueA === "number" ||
    typeValueA === "boolean" ||
    typeValueA === "string"
  ) {
    return valueA === valueB;
  }
  const isArray = Array.isArray(valueA) && Array.isArray(valueB);
  if (isArray) {
    if (valueA.length !== valueB.length) {
      return false;
    }
    for (let i = 0; i < valueA.length; i++) {
      if (!deepEqual(valueA[i], valueB[i])) {
        return false;
      }
    }
    return true;
  } else if (Array.isArray(valueA) || Array.isArray(valueB)) {
    return false;
  }
  const objAKeys = Object.keys(valueA);
  const objBKeys = Object.keys(valueB);
  if(objAKeys.length !== objBKeys){
    return false
  }
  for (const key in objAKeys) {
    if (!(Object.prototype.hasOwnProperty.call(valueB, key))) {
      return false;
    }
    if (!deepEqual(valueA[key], valueB[key])) {
      return false;
    }
  }
  return true;
}

console.log(
  deepEqual(
    deepEqual(
      { foo: "bar", item: [1, 2, { baz: "baz" }] },
      { foo: "bar", item: [1, 2, { baz: "baz" }], id: 1 },
    ),
  ),
);
