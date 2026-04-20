
// This is a JavaScript coding problem from BFE.dev 

/**
 * @param {(...args: any[]) => any} func
 * @param {number} wait
 * @returns {(...args: any[]) => any}
 */
function debounce(func, wait) {
  let timer;

  return function(...args){
    clearTimeout(timer);
    timer = setTimeout(()=>{
       func.apply(this, args);
    }, wait)
  }
}