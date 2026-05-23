## [104. Inheritance](https://bigfrontend.dev/quiz/Inheritance)

### Approach
In Javascript, inheritance is implemented using Prototype chain.

So basically, when trying to access a property of an object, the property will not only be sought on the object but on the prototype of the object, the prototype of the prototype, and so on until either a property with a matching name is found or the end of the prototype chain is reached.

Here, because B extends A, the following protoype chain gets formed.

b ---> B.prototype ---> A.prototype ---> Object.prototype ---> null
When accessing a.b, the property is not available on A and also not available on A.prototype thus returning undefined.

For the object b, all three properties are available—

a gets inherited from class A
b is defined in class B itself
c gets inherited from A.prototype