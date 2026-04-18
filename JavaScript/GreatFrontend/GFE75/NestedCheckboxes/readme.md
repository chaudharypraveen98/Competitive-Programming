## [Nested Checkboxes](https://www.greatfrontend.com/interviews/study/gfe75/questions/user-interface/nested-checkboxes)

### Approach
1. `useRef` to update `isdeterminate`.
2. use `backtracking` and update child first
3. use `id` check
4. once id is matched, update child acc