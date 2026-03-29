/**
 * @param {Array<string>} items
 * @param {{sorted?: boolean, length?: number, unique?: boolean}} [options]
 * @return {string}
 */
export default function listFormat(items, options = {}) {
  const { sorted = false, length = 0, unique = false } = options;
  let seen = new Set();
  items = items.filter((item) => {
    if (!item) return false;

    if (unique) {
      const isAlreadyPresent = seen.has(item);
      if (isAlreadyPresent) {
        return false;
      }
      seen.add(item);
    }
    return true;
  });
  if (!items.length) {
    return "";
  }
  if (sorted) {
    items = items.sort();
  }
  if (length && length > 0 && items.length > length) {
    return `${items.slice(0, length).join(", ")} and ${items.length - length} other${items.length - length === 1 ? "" : "s"}`;
  }
  return items.length > 1
    ? `${items.slice(0, items.length - 1).join(", ")} and ${items[items.length - 1]}`
    : items[0];
}


console.log(listFormat([])); // ''

console.log(listFormat(['Bob'])); // 'Bob'
console.log(listFormat(['Bob', 'Alice'])); // 'Bob and Alice'

console.log(listFormat(['Bob', 'Ben', 'Tim', 'Jane', 'John']));
// 'Bob, Ben, Tim, Jane and John'

console.log(listFormat(['Bob', 'Ben', 'Tim', 'Jane', 'John'], {
  length: 3,
})); // 'Bob, Ben, Tim and 2 others'

console.log(listFormat(['Bob', 'Ben', 'Tim', 'Jane', 'John'], {
  length: 4,
})); // 'Bob, Ben, Tim, Jane and 1 other'

console.log(listFormat(['Bob', 'Ben', 'Tim', 'Jane', 'John'], {
  length: 3,
  sorted: true,
})); // 'Ben, Bob, Jane and 2 others'

console.log(listFormat(['Bob', 'Ben', 'Tim', 'Jane', 'John', 'Bob'], {
  length: 3,
  unique: true,
})); // 'Bob, Ben, Tim and 2 others'

console.log(listFormat(['Bob', 'Ben', 'Tim', 'Jane', 'John'], {
  length: 3,
  unique: true,
})); // 'Bob, Ben, Tim and 2 others'

console.log(listFormat(['Bob', 'Ben', '', '', 'John'])); 