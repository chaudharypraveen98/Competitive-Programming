const obj = {}
const a = { name: 'a'}
const b = { name: 'b'}
obj[a] = {...a}
obj[b] = {...b}

console.log(obj[a].name)
console.log(obj[b].name)

// "b"
// "b"