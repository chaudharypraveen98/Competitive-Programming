## [126. Object.keys()](https://bigfrontend.dev/quiz/object-keys)

### Approach
Object.keys static method returns an array of a given object's own enumerable string-keyed property names. This means
```
Object.keys({a:1,b:2}) -> ["a","b"]
Object.keys({a:1,b:2}) -> ["b","a"]
```

Using spread operator on an array enumerates the keys into a single array before logging it.