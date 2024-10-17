/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
  if (!obj || typeof obj != "object") {
    return obj;
  }
  if (Array.isArray(obj)) {
    let temp = [];
    obj.forEach((item) => {
      const cal = compactObject(item);
      if (cal) {
        temp.push(cal);
      }
    });
    return temp;
  }
  let res = {};
  Object.keys(obj).forEach((key) => {
    const resolve = compactObject(obj[key]);
    if (resolve) {
      res[key] = resolve;
    }
  });
  return res;
};
