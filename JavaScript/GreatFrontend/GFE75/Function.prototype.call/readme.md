## [Function.prototype.call](https://www.greatfrontend.com/interviews/study/gfe75/questions/javascript/function-call)

### Approach

1. Context Wrapping: If a user passes a primitive (like (5).myCall(...)), standard call treats it as an Object. Object(thisArg) handles this conversion.
2. The Symbol: Using a Symbol is much safer than a string like context.tempFn = this. If the object already had a property named tempFn, you would accidentally overwrite it. Symbols are guaranteed to be unique.
3. The Property Call: The line context[fnSymbol](...argArray) is where the magic happens. Because the function is now a property of context, JavaScript sets the internal this of the function to that context.