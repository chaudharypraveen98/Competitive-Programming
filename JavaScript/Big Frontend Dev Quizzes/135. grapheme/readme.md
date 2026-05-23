## [135. grapheme](https://bigfrontend.dev/quiz/property-key-and-value)

### Approach
```
const str = "BFE👍" // 👍 is taken as 2 chars as unicode
console.log(str.length) // 5
console.log(str.slice(3, 4) == '👍') // false this take first char of unicode
console.log([...str].length) //4  ["B","F","E", "👍"]
console.log([...str].slice(3, 4) == '👍') // true as last element of array
```