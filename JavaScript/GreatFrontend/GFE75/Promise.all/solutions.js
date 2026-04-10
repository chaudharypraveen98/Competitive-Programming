/**
 * @param {Array} iterable
 * @return {Promise<Array>}
 */
export default function promiseAll(iterable) {
  if(iterable.length===0){
    return Promise.resolve([])
  }

  return new Promise((resolve, reject)=>{
    let results = [];
    let completed = 0;

    iterable.forEach((promise, index)=>{
        Promise.resolve(promise).then((val)=>{
            results[index] =val;
            completed++;
            if(completed===iterable.length){
                resolve(results)
            }
        }).catch((error)=>{
            reject(error)
        })
    })
  })
}