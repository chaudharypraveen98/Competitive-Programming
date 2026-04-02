export function isArray(value) {
  return Array.isArray(value)
}

export function isFunction(value) {
  return typeof value=== 'function'
}

export function isObject(value) {
  const type = typeof value;
  return value !== null && (type === 'object' || type === 'function');
}

export function isPlainObject(value) {
  if(value===null || typeof value !== 'object'){
    return false
  }
  const proto = Object.getPrototypeOf(value)

  return proto === null || proto === Object.prototype
}