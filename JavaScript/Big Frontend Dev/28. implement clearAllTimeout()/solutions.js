/**
 * cancel all timer from window.setTimeout
 */
const window  = global;
let timers = new Set();
const oldSetTimeout = window.setTimeout;
const oldClearTimeout = window.clearTimeout;
window.setTimeout = function(callback, delay,...args){
    const currentTimerId = oldSetTimeout.call(this, (...callbackArgs)=>{
        timers.delete(currentTimerId)
        callback.apply(this, callbackArgs)

    }, delay, ...args);
    timers.add(currentTimerId)
    return currentTimerId
}
window.clearTimeout = function(id) {
  timers.delete(id);
  oldClearTimeout(id);
};
function clearAllTimeout() {
  for(const tId of timers){
    clearTimeout(tId)
  }
  timers.clear()
}
const func1=()=>{
    console.log("fun1")
}
const func2=()=>{
    console.log("fun2")
}
const func3=()=>{
    console.log("fun3")
}

setTimeout(func1, 10000)
setTimeout(func2, 10000)
setTimeout(func3, 10000)
// all 3 functions are scheduled 10 seconds later
clearAllTimeout()