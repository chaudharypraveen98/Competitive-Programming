function memoize(func, resolver) {
  // 1. Validation (Internal Lodash check)
  if (typeof func !== 'function' || (resolver != null && typeof resolver !== 'function')) {
    throw new TypeError('Expected a function');
  }

  // 2. The actual memoized wrapper
  const memoized = function(...args) {
    // 3. INTERNAL KEY LOGIC: Defaults to args[0] if no resolver
    const key = resolver ? resolver.apply(this, args) : args[0];
    const cache = memoized.cache;

    if (cache.has(key)) {
      return cache.get(key);
    }
    
    const result = func.apply(this, args);
    
    // 4. Update the exposed cache
    memoized.cache = cache.set(key, result) || cache;
    return result;
  };

  // 5. Initialize the cache (Lodash uses a custom Map wrapper)
  memoized.cache = new (memoize.Cache || Map)();
  
  return memoized;
}

// Lodash allows you to globally change the Cache constructor
memoize.Cache = Map;