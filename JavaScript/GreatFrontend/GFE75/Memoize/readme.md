## [Memoize](https://www.greatfrontend.com/interviews/study/gfe75/questions/javascript/memoize)


#### One Final "Interview" Warning: The JSON.stringify Trap
If an interviewer wants to push you to the limit, they will ask: "What happens if two different arguments produce the same JSON string?"

The Collision Example:
```
const myFunc = (a) => a;
const memFunc = memoize(myFunc);

memFunc({ a: undefined }); // JSON.stringify turns this into "{}"
memFunc({ b: undefined }); // JSON.stringify also turns this into "{}"
// Result: The second call returns the cached value of the first, 
// even though the objects are different!
```

The "Pro" Answer: > "In a production library like Lodash, the default behavior is often to only use the first argument as the key. If multiple arguments are needed, we suggest the user provide a custom resolver that handles their specific data types safely, or we use a more robust 'Trie' (nested Map) structure to avoid stringification entirely."


#### Lodash : The "Gotcha" Example
Because Lodash only uses the first argument, you can run into this common bug:

```
const add = (a, b) => a + b;
const memoAdd = _.memoize(add);

memoAdd(1, 2); // Key is 1, Result is 3
memoAdd(1, 5); // Key is 1, Returns CACHED 3 (Incorrect!)
```


#### Memoization Strategy Comparison

| Strategy                | Accuracy                             | Multi-Arg Support         | Memory Leak Risk              | Best Use Case                                               |
|-------------------------|--------------------------------------|---------------------------|-------------------------------|-------------------------------------------------------------|
| JSON.stringify          | ❌ Low (Collisions on {a:1} vs {a:1}) | ✅ Yes (Auto-stringified)  | ⚠️ High (Strings stay in Map) | Quick prototyping or simple string/number arguments.        |
| First Arg Only          | ✅ High (Reference check)             | ❌ No (Ignores extra args) | ⚠️ High (Uses regular Map)    | High-performance React selectors (e.g., memoize-one).       |
| Flat Map (Manual Key)   | ✅ High (User-defined)                | ⚠️ Manual (Via resolver)  | ⚠️ High (Uses regular Map)    | When you have a unique ID (like user.id) to use as a key.   |
| Pure WeakMap Trie       | ✅ High (Reference check)             | ✅ Yes (Recursive)         | ✅ Zero (Auto-GC)              | Functions that only take Objects as arguments.              |
| Hybrid Trie (Your Code) | ✅ Highest                            | ✅ Full Support            | ✅ Zero                        | Production-grade utility libraries and complex state logic. |
