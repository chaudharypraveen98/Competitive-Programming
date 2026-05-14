// This is a JavaScript Quiz from BFE.dev

var a = 1
function a() {
}

console.log(typeof a)

var b
function b() {
}
b = 1

console.log(typeof b)

function c() {
}
var c = 1;

console.log(typeof c)

var d = 1;

(function(){
  d = '2'
  console.log(typeof d)
  function d() {
  }
})()

console.log(typeof d)

var e = 1
const f = function e() {}

console.log(typeof e)

// "number"
// "number"
// "number"
// "string"
// "number"
// "number"