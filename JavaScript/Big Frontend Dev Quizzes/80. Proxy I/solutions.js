// This is a JavaScript Quiz from BFE.dev 

const obj = new Map()
const map = new Map()
obj.foo = 1
map.set('foo', 2)
console.log(obj.foo)
console.log(map.get('foo'))

const proxyObj = new Proxy(obj, {})
const proxyMap = new Proxy(map, {})
console.log(proxyObj.foo)
console.log(proxyMap.get('foo'))

// 1
// 2
// 1
// Error