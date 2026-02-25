/**
 * @param {Function} func
 * @param {number} wait
 * @return {Function}
 */
export default function debounce(func, wait) {
  let timer;

  // ...args collect all the args
  return function(...args){
    clearTimeout(timer);
    timer = setTimeout(()=>{
      // we need to pass this reference
      func.apply(this, args)
    }, wait)
  }
}