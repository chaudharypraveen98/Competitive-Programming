
/**
 * @param {object[]} items
 * @excludes { Array< {k: string, v: any} >} excludes
 */

/**
 * @param {object[]} items
 * @param { Array< {k: string, v: any} >} excludes
 * @return {object[]}
 */
function excludeItems(items, excludes) {
   const excludeMap =new Set(excludes.map((item)=>`${item.k}_${item.v}`))

   return items.filter((item)=>{
     return !Object.keys(item).some((k)=>{
        if(excludeMap.has(`${k}_${item[k]}`)){
            return true
        }
        return false
     })
   })
}

// Given an input of array, 
// which is made of items with >= 3 properties
let items = [
  {color: 'red', type: 'tv', age: 18}, 
  {color: 'silver', type: 'phone', age: 20},
  {color: 'blue', type: 'book', age: 17}
] 
// an exclude array made of key value pair
const excludes = [ 
  {k: 'color', v: 'silver'}, 
  {k: 'type', v: 'tv'}, 
] 

console.log(excludeItems(items, excludes))