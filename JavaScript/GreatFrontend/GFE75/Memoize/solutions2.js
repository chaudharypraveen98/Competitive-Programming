export default function memoize(func, resolver) {
  let root = {
    primitives: new Map(),
    objects: new WeakMap(),
  };

  const RESULT_KEY = Symbol("result");

  const memoizedFunc = function (...args) {
    let curr = root;
    for (const arg of args) {
      const isObject =
        arg !== null && (arg instanceof Function || typeof arg === "object");
      const container = isObject ? curr.objects : curr.primitives;

      if (!container.has( arg)) {
        container.set(arg, {
          primitives: new Map(),
          objects: new WeakMap(),
        });
      }

      curr = container.get(arg)
    }
    // leaf node
    if( RESULT_KEY in curr){
        return curr[RESULT_KEY]
    }
    const res = func.apply(this, args)
    curr[RESULT_KEY]= res
    return res
  };

  memoizedFunc.cache = root;
  return memoizedFunc;
}
