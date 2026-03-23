/**
 * @template T
 * @param {T} value
 * @return {T}
 */
export default function deepClone(value, map = new WeakMap()) {
  if (value === null || typeof value !== "object") {
    return value;
  }
  if (map.has(value)) return map.get(value);
  if (value instanceof Date) {
    return new Date(value);
  }
  if (value instanceof RegExp) {
    return new RegExp(value.source, value.flags);
  }
  if (value instanceof Set) {
    const clonedSet = new Set();
    map.set(value, clonedSet);
    value?.forEach((item) => clonedSet.add(deepClone(item, map)));
    return clonedSet;
  }

  if (value instanceof Map) {
    const clonedMap = new Map();
    map.set(value, clonedMap);
    value?.forEach((val, key) => clonedMap.set(deepClone(key, map),deepClone(val, map)));
    return clonedMap;
  }

  let clonedObj = Array.isArray(value) ? [] : {};
  map.set(value, clonedObj)
  Reflect.ownKeys(value).forEach((key) => {
    clonedObj[key] = deepClone(value[key], map);
  });

  return clonedObj;
}

const obj1 = { user: { role: "admin" } };
const clonedObj1 = deepClone(obj1);
console.log(clonedObj1);

clonedObj1.user.role = "guest"; // Change the cloned user's role to 'guest'.
clonedObj1.user.role; // 'guest'
console.log(obj1.user.role); // Should still be 'admin'.

const obj2 = { foo: [{ bar: "baz" }] };
const clonedObj2 = deepClone(obj2);

obj2.foo[0].bar = "bax"; // Modify the original object.
obj2.foo[0].bar; // 'bax'
console.log(clonedObj2.foo[0].bar); // Should still be 'baz'.
