var TimeLimitedCache = function () {
  this.cache = {};
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  const found = key in this.cache;
  if (found) {
    clearTimeout(this.cache[key].ref);
  }
  this.cache[key] = {
    val: value,
    ref: setTimeout(() => {
      delete this.cache[key];
    }, duration),
  };
  return found;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  return key in this.cache ? this.cache[key].val : -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return Object.keys(this.cache).length;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
