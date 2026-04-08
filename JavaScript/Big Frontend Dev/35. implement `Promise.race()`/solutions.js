
/**
 * @param {Array<Promise>} promises
 * @return {Promise}
 */
function race(promises) {
  if(promises.length===0){
    return Promise.resolve([])
  }

  return new Promise((resolve, reject)=>{
    promises.forEach((promise)=>{
        return promise.then((val)=>{
            resolve(val)
        }).catch((reason)=>{
            reject(reason)
        })
    })
  })
}