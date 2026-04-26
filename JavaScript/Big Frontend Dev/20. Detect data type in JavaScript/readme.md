## [20. Detect data type in JavaScript](https://bigfrontend.dev/problem/detect-data-type-in-JavaScript)

### Approach
1. `Object.prototype.toString.call(value)` returns strings like [object Null], [object Map], [object Date], etc. — so slicing out the middle part and lowercasing it handles every case in one line.