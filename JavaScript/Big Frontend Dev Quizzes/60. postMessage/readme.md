## [60. postMessage](https://bigfrontend.dev/quiz/postMessage)

### Approach
1. MessageChannel interface of the Channel Messaging API allows us to create a new message channel and send data through it
2. Promise.resolve() method returns a Promise object that is resolved with a given value.
3. setTimeout() method sets a timer which executes a function or specified piece of code once the timer expires. These tasks are queued to the Macrotask Queue
4. Since JS is single-threaded, the main thread can only execute one statement at a time. The order in which this execution happens is—
5. First all synchronous tasks are queued
6. The micro task queue (promises, worker threads, messaagechannel) will execute immediately when the JS run stack is empty
7. The priority of macro task queue is lower than that of micro task queue
8. So here, first the synchronous statement 1 gets logged. Then onmessage handler gets associated with messagechannel. 3 is a resolved promise so it's added to the microtask queue. setTimeout of 4 is added to macrotask queue. 5 is a synchronous statement so it gets printed second. Using postMessage we trigger the handler and 2 gets added to micro task queue. Lastly, 6 is a synchronous statement so it gets printed third.
9. Now, since the main call stack is empty, microtask queue tasks are executed (as they have higher priority over macrotask queue). Hence, order in which they get printed is 1 -> 5 -> 6 -> 3 -> 2 -> 4