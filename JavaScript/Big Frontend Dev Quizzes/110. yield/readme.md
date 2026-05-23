## [110. yield](https://bigfrontend.dev/quiz/yield)

### Approach
Both genA and genB are Generators functions that can be exited and later re-entered

yield keyword pauses generator function execution and the value of the expression following the yield keyword is returned to the generator's caller.

On the other hand, yield* expression iterates over the operand and yields each value returned by it.

Here, the generator function genA has a single yield statement so it returns [1, 2, 3]. But in genB, we use yield* so it returns array elements one by one hence logging the first element i.e. 1

