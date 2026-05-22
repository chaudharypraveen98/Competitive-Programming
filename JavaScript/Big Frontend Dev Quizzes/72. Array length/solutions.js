class MyArray extends Array {
  get length() {
    return 3 // this will not override parent's length
  }
}
const arr1 = new MyArray(10)
console.log(arr1.length) // 10
const arr2 = new Array(10)
console.log(arr2.length) // 10

// 10
// 10