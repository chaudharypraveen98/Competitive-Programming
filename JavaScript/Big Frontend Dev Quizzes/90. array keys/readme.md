## [90. array keys](https://bigfrontend.dev/quiz/array-keys)


### Approach
The static `Reflect.ownKeys()` method returns an array of the target object's own property keys.

Arrays under the hood in JavaScript are Objects. Their keys are numbers, and their values are the elements. By default, all arrays also have a property length that reflects the number of elements in that array. In the case of a sparse array, holes do not add the corresponding key to the array.

Also, the spread operator converts these holes to undefined

1. Its an empty array so answer only contains length

2. This array `[,]` is also an empty sparse array hence holes are ignored

3. `[1,,2]` has values defined at index 0 and 2, hence it prints `["0","2","length"]`

4. Using Spread Operator changes the input array to `[1,undefined,2]` thus all the keys give following output `["0","1","2","length"]`

## Meta-Programming

1. Core Architectural Concepts: Meta-Programming
The Proxy and Reflect APIs, introduced in ES6, provide first-class support for meta-programming in JavaScript—the ability to inspect, intercept, and modify the language's fundamental operations using the language itself.

The Proxy API: Acts as an architectural wrapper around a target object. It allows you to intercept and override default behaviors for low-level operations, such as property lookups (get), property assignments (set), and property deletions (deleteProperty).

The Reflect API: A global object that provides a 1:1 mapping of static methods for every single interceptable Proxy trap. It implements standard JavaScript runtime behavior.

2. The "Why": Why combine Proxy with Reflect?
When intercepting an operation within a Proxy trap, you often want to fallback or execute the default language behavior after running your custom logic.

Instead of manually writing target[key] = value (which can break edge cases like inherited prototype setters or customized receiver contexts), you forward the arguments cleanly via the Reflect API: Reflect.set(target, key, value, receiver). This guarantees referential and semantic safety.

```
┌────────────────────────────────────────────────────────┐
│                      PROXY WRAPPER                     │
│                                                        │
│   Incoming Operation ──► Custom Interceptor (Trap)     │
│                                  │                     │
│                                  ▼                     │
│                       [ Run Architectural Logic ]      │
│                                  │                     │
│                                  ▼                     │
│   Target Object  ◄───────  Reflect API                 │
│  (Default Action)         (Forward Arguments)          │
└────────────────────────────────────────────────────────┘
```

3. Structuring a Proxy: Syntax & Traps
The Proxy constructor takes two arguments: the baseline target object and a handler configuration object containing the interceptor functions ("traps").

```
const proxy = new Proxy(target, handler); //
```

### The Core Traps Matrix
While there are over a dozen traps available, senior UI engineering heavily leverages three primary operations:

| Trap Signature                     | Intercepted Action                              | Senior Engineering Use Case                                     |
|------------------------------------|-------------------------------------------------|-----------------------------------------------------------------|
| get(target, prop, receiver)        | Reading a property value (obj.prop).            | Dynamic default fallbacks, schema routing, or logging.          |
| set(target, prop, value, receiver) | Writing a property value (obj.prop = val).      | Production-grade runtime type-checking and schema validation.   |
| has(target, prop)                  | The in operator operator check ('prop' in obj). | Hiding sensitive system-level state or masking underlying keys. |
