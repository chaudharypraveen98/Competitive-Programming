## Approaches 

We will be using using deque has it has constant push and removal
1. Using two queues
   * Concept is simple, we will do the push and is empty check on q1
   * for top we will first pop all the elements excpet the last one , store it and pop and append to q2 and swap
   * for pop , as we have stored the values in queue, and we can pop from the start , we start popping all the values and appending to q2 except the last one just pop 
2. Using single queue
   * We just try to maintain the stack while insertion , once new element is added , it is added at the last as queue behaviour, element before that starting from the start will be poppped and inserted at the back