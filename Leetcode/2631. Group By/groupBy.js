/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  let res = {};

  this.forEach((item) => {
    const key = fn(item);
    if (key in res) {
      res[key].push(item);
    } else {
      res[key] = [item];
    }
  });
  return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
