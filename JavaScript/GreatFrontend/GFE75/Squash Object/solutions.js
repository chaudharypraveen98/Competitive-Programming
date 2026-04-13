/**
 * @param {Object} obj
 * @return {Object}
 */
export default function squashObject(obj) {
    const finalObj = {};
    function process(processObj, str = "") {
        if (typeof processObj !== "object" || processObj === null) {
            finalObj[str] = processObj;
            return processObj;
        }
        for (const key of Object.keys(processObj)) {
            const newKey = str && key ? `${str}.${key}` : key || str ;
            process(processObj[key], newKey);
        }
    }
    process(obj);
    return finalObj;
}

const object = {
    foo: {
        "": {
            "": 1,
            bar: 2,
        },
        a: 1,
    },
};

console.log(squashObject(object)); // { a: 5, b: 6, 'c.f': 9, 'c.g.m': 17, 'c.g.n': 3 }
