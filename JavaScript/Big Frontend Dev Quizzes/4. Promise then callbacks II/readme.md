## [4. Promise then callbacks II](https://bigfrontend.dev/quiz/4-Promise-then-callbacks-II)

### Approach
1.  .catch() swallows errors and returns a resolved promise (undefined) by default.
2.  .finally() is transparent; it ignores return values and passes the previous fulfillment value through to the next handler.
3.  Nested Promises are awaited; the parent .then() will not resolve until the returned inner Promise settles.