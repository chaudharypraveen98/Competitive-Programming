## [7. implement debounce() with leading & trailing option](https://bigfrontend.dev/problem/implement-debounce-with-leading-and-trailing-option)


### Approach
1. `option.trailing && !isLeading`, is the "guard" that prevents your function from firing twice for a single event when both leading and trailing options are enabled.
   1. option.trailing: "Should I fire at the end of the wait period?" 
   2. isLeading: "Did I already fire at the very start of this specific wait period?"