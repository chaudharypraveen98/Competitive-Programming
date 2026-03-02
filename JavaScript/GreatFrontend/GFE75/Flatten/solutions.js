/**
 * @param {Array<*|Array>} value
 * @return {Array}
 */
export default function flatten(value) {
    let result = []
    function flattenHelper (item){
        if(Array.isArray(item)){
            for(let i=0; i < item.length; i++){
                if(i in item){
                    flattenHelper(item[i])
                }
            }
        } else {
            result.push(item)
        }
    }
    flattenHelper(value)
    return result
}

// Single-level arrays are unaffected.
console.log(flatten([1, 2, 3])); // [1, 2, 3]

// Inner arrays are flattened into a single level.
console.log(flatten([1, [2, 3]])); // [1, 2, 3]
console.log(flatten([
  [1, 2],
  [3, 4],
])); // [1, 2, 3, 4]

// Flattens recursively.
console.log(flatten([1, [2, [3, [4, [5]]]]])); // [1, 2, 3, 4, 5]
