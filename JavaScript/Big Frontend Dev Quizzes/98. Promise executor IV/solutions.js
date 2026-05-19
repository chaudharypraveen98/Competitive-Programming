const promise = new Promise((resolve, reject) => {
  const promise2 = Promise.reject('error').then(() => {
    console.log(1)
  }, () => {
    console.log(2)
  })
  resolve(promise2)
});
promise.then(console.log);

// 2
// undefined