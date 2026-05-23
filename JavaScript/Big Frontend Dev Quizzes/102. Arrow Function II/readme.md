## [102. Arrow Function II](https://bigfrontend.dev/quiz/Arrow-Function-II)

### Approach
Normal Function — the value of this is determined by how a function is called i.e. runtime binding.

Arrow Function — don't provide their own this binding; it retains the this value of the enclosing lexical context i.e. static binding.

Here, we've declared a class Site and within this class property this.name will refer to outer name. Then, we declare a class method getHandle which returns another object with a local property name.

Both getName1 and getName3 are normal functions. When a function is called as a method of an object, its this is set to the object the method is called on which means this.name will be bigfrontend

getName2 on the other hand is an arrow function hence it will basically borrow the scope from outside this returned object which means this.name will be BFE