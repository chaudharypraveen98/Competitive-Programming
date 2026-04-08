
/**
 * @param {Array<Promise>} promises
 * @return {Promise}
 */
function any(promises) {
  if(promises.length===0){
    return Promise.reject(new AggregateError('All promises were rejected',[] ));
  }
  return new Promise((resolve, reject)=>{
    let proccessed = 0;
    let rejectReasons = [];
    promises.forEach((promise,index)=>{
        Promise.resolve(promise).then((val)=>{
            resolve(val)
        }).catch((reason)=>{
            rejectReasons[index] = reason;
            proccessed++;
            
            if(proccessed===promises.length){
                reject(new AggregateError( 'All promises were rejected', rejectReasons));
            }
        })
    })
  })
}