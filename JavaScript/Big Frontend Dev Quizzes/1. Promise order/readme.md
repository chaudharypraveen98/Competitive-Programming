## [1. Promise order](https://bigfrontend.dev/quiz/1-promise-order)


### Approach
1. `console.log(1)` // sync task -> printed same time
2. promise declaration -> will be printed at same time
```
const promise = new Promise((resolve) => {
    console.log(2); // 2 immediately
    resolve();
    console.log(3); // 3 immediately
});
```
3. `console.log(4)` // sync task -> printed same time
4. this is micro task, will be picked between any event loop cycle
```
promise
    .then(() => {
        console.log(5);
    })
    .then(() => {
        console.log(6);
    });

```
5. `console.log(7)` : // sync task -> printed same time
6. Will be picked only in next event loop cycle, after promise resolving
```
setTimeout(() => {
  console.log(8)
}, 10)
```
7. Same with it as above but will be before above one because it has zero timer value
```
setTimeout(() => {
  console.log(9)
}, 0)
```


### Answer
```
1
2
3
4
7
5
6
9
8
```