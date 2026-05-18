// This is a JavaScript Quiz from BFE.dev

var obj = {
  a: "BFE",
  b: "dev",
  func: (function foo(){ return this.a; }, function bar(){ return this.b; })
}

console.log(obj.func())

"dev"