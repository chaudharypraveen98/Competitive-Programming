## [8. can you shuffle() an array?](https://bigfrontend.dev/problem/can-you-shuffle-an-array)

### Approach
1. [Solution 1](./solutions.js) - use simple random with splice and new array creation. Time - O(n2) and Space - O(n)
2. [Solution 1](./solutions2.js) - uses sort but it will result in bias solution. Time - O(nlogn) and Space - O(n)
3. [Solution 2](./solutions3.js) - use The gold standard for shuffling is the [Fisher-Yates algorithm](https://www.youtube.com/watch?v=4zx5bM2OcvA). It is perfectly unbiased and runs in $O(n)$ time. 