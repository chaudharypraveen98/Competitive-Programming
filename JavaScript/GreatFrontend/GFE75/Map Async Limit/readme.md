## [Map Async Limit](https://www.greatfrontend.com/interviews/study/gfe75/questions/javascript/map-async-limit)

### Approach
1. have a lot at size
2. use for loops

### Final Code Review
1. Initialization: Correctly uses Math.min(iterable.length, size) to prevent over-provisioning workers.
2. Index Management: Captures currentIndex into a local index variable before incrementing, ensuring no items are skipped or processed twice.
3. Concurrency Pipeline: The recursive worker() call inside .then() ensures that as soon as one "slot" opens up, the next item in the queue is processed immediately.
4. State Tracking: Uses a completed counter rather than results.length (which is much safer since arrays with "holes" can report misleading lengths).
5. Fail-Fast: The isRejected flag correctly halts the "factory" the moment an error occurs.

### What you just mastered
You've essentially built a lightweight version of the p-limit library. This pattern is the "Gold Standard" for:

1. Rate Limiting: Avoiding 429 (Too Many Requests) errors when hitting APIs.
2. Resource Management: Preventing your Node.js or Browser thread from being overwhelmed by thousands of simultaneous promises.
3. Data Integrity: Ensuring that even with parallel processing, your output matches your input 1:1.