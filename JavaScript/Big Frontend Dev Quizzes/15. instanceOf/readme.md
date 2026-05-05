## [15. instanceOf](https://bigfrontend.dev/quiz/instanceOf)

### The "Why": Core Concepts
1. **typeof**: This operator returns a string indicating the type of the unevaluated operand. It is generally reliable for primitives but famously has historical quirks (like null). 
2. **instanceof**: This operator tests whether the .prototype property of a constructor appears anywhere in the prototype chain of an object. Crucially, it only works on objects. If you use it on a primitive, it will always return false. 


### Step-by-Step 
1. **Execution1. The Null Paradox**
   1. `typeof null` --> `"object"`: A well-known historical bug in JavaScript where null was represented with the same type tag as objects. 
   2. `null instanceof Object` --> `false`: Despite what typeof says, null is a primitive and not an instance of Object. 
2. **Primitives vs. Wrapped Objects (Number & Boolean)**
   1. `typeof 1` --> `"number"`: 1 is a primitive number. 
   2. `1 instanceof Number / 1 instanceof Object` --> `false`: Primitives are not objects and do not have a prototype chain for instanceof to traverse. 
   3. `Number(1) instanceof Object` --> `false`: Calling Number(1) without the new keyword simply performs type conversion, returning a primitive. 
   4. `new Number(1) instanceof Object` --> `true`: Using the new keyword creates a wrapper object, which is an instance of both Number and Object. The same logic applies to true and the Boolean constructor.
3. **Real Objects (Arrays and Functions)**
   1. `[] instanceof Array` --> `true`: An array is a specialized object whose prototype chain includes Array.prototype. 
   2. `[] instanceof Object` --> `true`: Because Array.prototype itself inherits from Object.prototype. 
   3. `(() => {}) instanceof Object` --> `true`: Functions are also objects in JavaScript and sit on the Object prototype chain. 