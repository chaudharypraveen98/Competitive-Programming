/**
 * @param {Array<any>} promises - notice that input might contains non-promises
 * @return {Promise<Array<{status: 'fulfilled', value: any} | {status: 'rejected', reason: any}>>}
 */
function allSettled(promises) {
    if(promises?.length===0){
        return Promise.resolve([])
    }

    return new Promise((resolve, reject)=>{
        let settled = 0;
        let results = [];

        promises.forEach((promise, index)=>{
            Promise.resolve(promise).then((val)=>{
                results[index] = {
                    status: 'fulfilled',
                    value:val
                }
            }).catch((error)=>{
                 results[index] = {
                    status: 'rejected',
                    reason:error
                }
            }).finally(()=>{
                settled++;
                if(settled === promises.length){
                    resolve(results)
                }
            })
        })
    })
}
