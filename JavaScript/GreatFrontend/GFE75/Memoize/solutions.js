/**
 * @param {Function} func
 * @returns Function
 */
export default function memoize(func, resolver) {
  let cache = new Map();
  const memoizedFunction = function (...args) {
    const key = resolver ? resolver.apply(this, args) : JSON.stringify(args);
    if (cache.has(key)) {
      return cache.get(key);
    } else {
      const res = func.apply(this, args);
      cache.set(key, res);
      return res;
    }
  };

  memoizedFunction.cache = cache;
  memoizedFunction.clear = () => cache.clear();
  return memoizedFunction;
}

function expensiveFunction(n) {
  console.log("Computing...");
  return n * 2;
}

// Create a memoized version of the function.
const memoizedExpensiveFunction = memoize(expensiveFunction);

// First call (computes and caches the result).
console.log(memoizedExpensiveFunction(5)); // Output: Computing... 10

// Second call with the same argument (returns the cached result).
console.log(memoizedExpensiveFunction(5)); // Output: 10

// Third call with a different argument (computes and caches the new result).
console.log(memoizedExpensiveFunction(10)); // Output: Computing... 20

// Fourth call with the same argument as the third call (returns the cached result).
console.log(memoizedExpensiveFunction(10)); // Output: 20
