## [123. return in Generator 2](https://bigfrontend.dev/quiz/return-gen)

### Approach
In this example, we have a generator function g which is invoked when we run g(). However, this does not immediately start the execution but rather pauses it.

obj.next() will resume the generator and we see 1 logged to console. Next up, we see 2 logged as the try block gets executed. The yield keyword will yield the value 2 and generator is paused again.

obj.return i.e. Generator.return() method acts as if a return statement is inserted in the generator's body at the current suspended position. This finishes the generator and allows the generator to move on to the finally block. Hence, 4 gets logged.