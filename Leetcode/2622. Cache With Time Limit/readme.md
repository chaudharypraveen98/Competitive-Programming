Link -> [2622. Cache With Time Limit](https://leetcode.com/problems/cache-with-time-limit/?envType=study-plan-v2&envId=30-days-of-javascript)

## Approach
1. Initialize the object with cache
2. Use setTimeout to remove items from the cache.
3. If a key already exists in the cache, cancel its timeout.
4. Overall time/space complexity: O(n)
5. Hurray ! Done
