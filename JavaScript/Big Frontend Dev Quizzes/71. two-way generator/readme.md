## [71. two-way generator](https://bigfrontend.dev/quiz/generator-2-way)

### Approach
1. With a generator function, values are not evaluated until they are needed. Therefore a generator allows us to define a potentially infinite data structure.
2. The next() method returns an object with two properties done and value. You can also provide a parameter to the next method to send a value to the generator. The value will be assigned as a result of a yield expression.
3. Because Grouping Operator gets evaluated first, the generator function gen yields/returns 100
4. Since we have passed 1 to the next() method. yield 100 is basically replaced with 1 and it returns 2*1 = 2
5. Since generator is completed it returns undefined