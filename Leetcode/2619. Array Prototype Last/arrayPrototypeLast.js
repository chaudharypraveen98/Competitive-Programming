/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function () {
  return this.length > 0 ? this.at(-1) : -1;
};
/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
