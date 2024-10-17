/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */

var join = function (arr1, arr2) {
  let result = {};
  // 1. initialization
  arr1.forEach((item) => {
    result[item.id] = item;
  });
  // 2. joining
  arr2.forEach((item) => {
    if (result[item.id]) {
      Object.keys(item).forEach((key) => {
        result[item.id][key] = item[key];
      });
    } else {
      result[item.id] = item;
    }
  });
  return Object.values(result);
};
