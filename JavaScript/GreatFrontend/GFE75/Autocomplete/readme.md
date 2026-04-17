## [Autocomplete](https://www.greatfrontend.com/interviews/study/gfe75/questions/system-design/autocomplete)


### Approach
1. Use `debouce` to save hits
2. use cache - `new Map`
3. use `retry` with `Timeout` with fetch
4. use `useCallback` on debounce function