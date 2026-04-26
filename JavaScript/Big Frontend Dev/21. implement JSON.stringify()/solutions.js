
/**
 * @param {any} data
 * @return {string}
 */
function stringify(data) {
    if (typeof data === "function" || typeof data === "symbol") {
        return undefined;
    }
    if (typeof data === "bigint") {
        throw new Error("Can't convert");
    }
    if (data === null || typeof data !== "object") {
        return typeof data === "string" ? `"${data}"` : String(data);
    }

    function process(node) {
        if (node === null || typeof node !== "object") {
            return typeof node === "string" ? `"${node}"` : String(node);
        }
        let res = [];
        const isArray = Array.isArray(node);
        if (isArray) {
            for (const item of node) {
                console.log("item", item, typeof item);
                if (
                    item === null ||
                    typeof item === "symbol" ||
                    item instanceof Symbol ||
                    typeof item === "function" ||
                    item === undefined
                ) {
                    res.push(null);
                } else {
                    res.push(process(item));
                }
            }
        } else {
            for (const [key, val] of Object.entries(node)) {
                if (
                    val === undefined ||
                    typeof val === "symbol" ||
                    typeof item === "function"
                ) {
                    continue;
                } else {
                    res.push(`"${key}":${process(val)}`);
                }
            }
        }
        const joined = res.join(",");
        return isArray ? `[${joined}]` : `{${joined}}`;
    }
    return process(data);
}

// console.log(stringify([1, 2, 3, 4]));
// console.log(
//     stringify({
//         a: 34,
//         b: {
//             c: 567,
//         },
//         d: {
//             random: true,
//         },
//         e: {
//             items: [1, 3, 4, null, { f: 123 }],
//         },
//         i: undefined,
//     }),
// );
console.log(stringify([Symbol("key")]));
// console.log(stringify(123n))
