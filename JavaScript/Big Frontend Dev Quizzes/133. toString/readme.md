## [133. toString](https://bigfrontend.dev/quiz/tostring)

### Approach
Here, we have created an object obj which will be an instance of Object and similarly function fun will be an instance of Function. Now lets breakdown each comparison:

1. obj.toString method is inherited from Object.prototype while Object.toString refers to the toString method directly on the Object constructor function itself. These both point to two different functions and hence log false
2. Since all functions in JavaScript inherit from Function.prototype, fun.toString is equivalent to the same method defined on Function.prototype. Thus, it logs true
3. Every object in JavaScript inherits properties and methods from its prototype. Since the prototype of any object is Object.prototype, obj.toString is equivalent to Object.prototype.toString. Logs true
4. Similar to 2. , all functions in JavaScript inherit from Function.prototype. Logs true
5. Object.toString is directly available on the Object constructor function itself while Object.prototype.toString method resides on the prototype of Object making each of them distinct entities. Logs false
6. Function.toString looks for the toString method on the Function object itself. If its not found there, it'll look up the prototype chain and find it on Function.prototype. Therefore, both expressions essentially point to the same method. Logs true

```
[ MEMORY HEAP LOOKUP TRAVERSAL ]

  obj (Object Instance) ─────► Object.prototype ───────────► [ Object.prototype.toString ]
                                                                     ▲
                                                                     │ (Inherits From)
  fun (Function Instance) ───► Function.prototype ─────────► [ Function.prototype.toString ]
                                     ▲                               ▲
                                     │ (Inherits From)               │
  Object (Constructor) ──────────────┘                               │
                                                                     │
  Function (Constructor) ────────────────────────────────────────────┘
```