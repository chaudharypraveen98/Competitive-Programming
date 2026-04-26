/**
 * @param {any} data
 * @return {string}
 */
function detectType(data) {
    const type = typeof data;
    if (data === null) {
        return "null";
    } else if (data === undefined) {
        return "undefined";
    } else if (type === "boolean" || data instanceof Boolean) {
        return "boolean";
    } else if (type === "string" || data instanceof String) {
        return "string";
    } else if (type === "number" || data instanceof Number) {
        return "number";
    } else if (type === "function" || type === "symbol" || type === "bigint") {
        return type;
    } else if (data instanceof Map) {
        return "map";
    } else if (data instanceof Set) {
        return "set";
    } else if (data instanceof Date) {
        return "date";
    } else if (data instanceof ArrayBuffer) {
        return "arraybuffer";
    } else if (Array.isArray(data)) {
        return "array";
    }
    return "object";
}
console.log(detectType(1)); // 'number'
console.log(detectType(new Map())); // 'map'
console.log(detectType([])); // 'array'
console.log(detectType(null)); // 'null'
