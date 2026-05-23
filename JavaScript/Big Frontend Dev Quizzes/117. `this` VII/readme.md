## [117. `this` VII](https://bigfrontend.dev/quiz/this-VII)

### Approach
static keyword in JS can be used to define class properties and method. The use of static implies a single shared copy available to all members of class and it's subclasses.

static properties can be directly accessed by the class.
class Book {
 static author = 'foo'
}

// is same as direct assignment to `Book` class.

```
class Book {}

Book.author = 'foo'

static method cannot be accessed directly by individual objects (subclasses)
class Book {
   static info() {}
}

Book.info() // correct. just like properties, methods can be accessed directly by class itself

const bookObj = new Book();
bookObj.info() // Error (not allowed)
```

So applying the above knowledge to our code snippet yield B.log() to print "BFE" (static property) and new B().log() to "bigfrontend" (non static method inheriting non static property)

```
class A {
  static dev = 'BFE'
  dev = 'bigfrontend'
}

class B extends A {
  log() {
    console.log(this.dev)
  }

  static log() {
    console.log(this.dev)
  }
}

B.log() // "BFE" <---
new B().log()// "bigfrontend" <---

```
