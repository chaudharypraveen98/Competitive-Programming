/**
 * @param {any} data
 * @return {string}
 */
function stringify(data) {
    const isInvalid = (v) => {
       return v === undefined || typeof v === "function" || typeof v === "symbol";
    };

    const formatPrimitiveValue = (v) => {
        if (typeof v === "string") return `"${v}"`;
        // isFinite - Infinity handling
        if (typeof v === "number") return isFinite(v) ? String(v) : "null";
        // big int
        if (typeof v === "bigint")
            throw new Error("Can't stringify big integer");
        if (v === null) return "null";
        return String(v);
    };

    function process(node) {
        if (node instanceof Date) {
            return `"${node.toISOString()}"`;
        }
        if (node === null || typeof node !== "object") {
            return formatPrimitiveValue(node);
        }
        const isArray = Array.isArray(node);
        if (isArray) {
            return `[${node
                .map((item) => {
                    if (isInvalid(item)) {
                        return "null";
                    } else {
                        return process(item);
                    }
                })
                .join(",")}]`;
        } else {
            return `{${Object.entries(node)
                .filter(([_, val]) => !isInvalid(val))
                ?.map(([key, val]) => {
                    return `"${key}":${process(val)}`;
                })
                ?.join(",")}}`;
        }
    }
    if (isInvalid(data)) return undefined;
    if (typeof data === "bigint")
        throw new Error("Can't stringify big integer");
    return process(data);
}
console.log(stringify([1, 2, 3, 4]));
console.log(
    stringify({
        a: 34,
        b: {
            c: 567,
        },
        d: {
            random: true,
        },
        e: {
            items: [1, 3, 4, null, { f: 123 }],
        },
        i: undefined,
    }),
);
console.log(stringify([Symbol("key")]));
console.log(stringify(123n));
