/**
 * @param {unknown} value
 * @returns {string}
 */
export default function jsonStringify(value) {
  if (value === null || typeof value !== "object") {
    return typeof value === "string" ? `"${value}"` : String(value);
  }
  function process(node) {
    if (node === null || typeof node !== "object") {
      return typeof node === "string" ? `"${node}"` : String(node);
    }
    const isArray = Array.isArray(node);
    const res = [];
    if (isArray) {
      for (const item of node) {
        if (
          item === undefined ||
          typeof item === "function" ||
          typeof item === "symbol"
        ) {
          res.push("null");
        } else {
          res.push(process(item));
        }
      }
    } else {
      for (const [key, value] of Object.entries(node)) {
        if (
          value === undefined ||
          typeof value === "function" ||
          typeof value === "symbol"
        ) {
          continue;
        } else {
          const returnedVal = process(value);
          res.push(`"${key}":${returnedVal}`);
        }
      }
    }
    const joinedValues = res.join(",");
    return isArray ? `[${joinedValues}]` : `{${joinedValues}}`;
  }

  return process(value);
}


console.log(jsonStringify({ foo: 'bar' })); // '{"foo":"bar"}'
console.log(jsonStringify({ foo: "bar", bar: [1, 2, 3] })); // '{"foo":"bar","bar":[1,2,3]}'
console.log(jsonStringify({ foo: true, bar: false })); // '{"foo":true,"bar":false}'
console.log(jsonStringify(null)); // 'null'
console.log(jsonStringify(true)); // 'true'
console.log(jsonStringify(false)); // 'false'
console.log(jsonStringify(1)); // '1'
console.log(jsonStringify('foo')); // '"foo"'
console.log(jsonStringify([null, null]))
