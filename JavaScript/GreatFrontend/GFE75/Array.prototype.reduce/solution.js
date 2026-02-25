/**
 * @template T, U
 * @param {(previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U} callbackFn
 * @param {U} [initialValue]
 * @return {U}
 */
Array.prototype.myReduce = function (callbackFn, initialValue) {
  if(typeof callbackFn !== 'function'){
    throw new TypeError(callbackFn+ " is not a fucntion")
  }

  // To make it work for array like structure like `this` -> "abc"
  const O = Object(this);

  // actually our reduce function also works for arr like structure like Array.prototype.myReduce.call({ length: "3.7", 0:1,1:2,2:3 }, (a,b)=>a+b)
  // It's a defensive approach , length may be string/float/NaN, uses spec LengthOfArrayLike it interanlly means safely convert to interger or throw error
  const len = O.length >>> 0;
  let acc;
  let i = 0;

  // check if intialValue is supplied
  if(arguments.length>1){
    acc = initialValue
  } else {
    // lets check sparse value and let index to first value index 
    while(i < len && !(i in O)) i++;
    if(i>=len){
      throw new TypeError("empty array without any intial value")
    }
    acc = O[i++]
  }
  for(i; i < len; i++){
    // i in O skips holes elision : These slots have no index and are not enumerable.
    if(i in O){
      acc = callbackFn(acc, O[i], i, this)
    }
  }
  return acc
};