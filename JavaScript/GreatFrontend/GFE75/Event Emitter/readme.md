## [Event Emitter](https://www.greatfrontend.com/interviews/study/gfe75/questions/javascript/event-emitter)

### Approach
1. `on` and `off` return this. `this` is useful for chaining.
2. duplicate listeners can be attached to single event name, deleting one will delete one only
3. `emit` will return true and false if it able to emit.