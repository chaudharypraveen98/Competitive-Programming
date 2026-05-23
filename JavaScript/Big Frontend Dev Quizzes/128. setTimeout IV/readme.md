## [128. setTimeout IV](https://bigfrontend.dev/quiz/settimeout-iv)

### Approach
Here, the behavior we observe is due to the use of a busy loop inside the block function. The while loop essentially locks the main thread, preventing it from processing other tasks, including the tasks scheduled by setTimeout. Breaking it down:

Logging 5 is a synchronous code, so its printed immediately
Then we schedule the execution of function a to occur after 0ms and b after 500ms. (Note that this just kinda starts the timer but hasn't pushed their callbacks to queue)
a gets executed first and 1 gets logged and block function as mentioned earlier, causes browser to be blocked for 1000ms (default duration in that function).
During this time, after 500ms timer for b has elapsed but as main thread is busy executing block so the callback is just waiting to be pushed to queue
Once block is completed, control is returned to a and next two timeouts are queued with respective delays 0ms and 1ms. At this moment, b also gets pushed to queue.
2 gets logged almost immediately as it has 0ms delay
Since timer for b was already over, 4 gets logged next
Lastly, the remaining callback 3 gets logged
As per my understanding, 4 should have been logged before 2 and 3, but here's where it gets complicated. Browsers may have different strategies for handling tasks scheduled with setTimeout and other asynchronous operations, leading to variations in the order of execution

In Chrome -> (5,1,2,4,3)

In Safari -> (5,1,4,2,3)