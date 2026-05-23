const items = [
  {
    id: 'a'
  },
  {
    id: 'b'
  },
]
const groups = Object.groupBy(items, ({id}) => id)
console.log(items.toString())
console.log(groups.toString())

// "[object Object],[object Object]"
// Error