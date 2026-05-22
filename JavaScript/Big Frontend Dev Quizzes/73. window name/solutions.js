
// This is a JavaScript Quiz from BFE.dev

var a = 1;
(function() {
  console.log(a + this.a);
  var a = '2'
  console.log(a + this.a);
})();

var name = 1; // implicitly coerced to string "1"
(function() {
  console.log(name + this.name);
  var name = '2'
  console.log(name + this.name);
})();

// NaN
// "21"
// "undefined1"
// "21"