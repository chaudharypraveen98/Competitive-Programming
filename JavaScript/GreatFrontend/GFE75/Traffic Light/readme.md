## [Traffic Light](https://www.greatfrontend.com/interviews/study/gfe75/questions/user-interface/traffic-light)

### Approach
1. Simply remember way to move yellow to green and yellow to red
2. use interval with clean up function
3. use prev

### You can even use config logic with next

```
const LIGHTS = {
  red: { duration: 4000, next: "yellow-green" },
  "yellow-green": { duration: 500, next: "green" }, // Yellow going to Green
  green: { duration: 3000, next: "yellow-red" },
  "yellow-red": { duration: 500, next: "red" },    // Yellow going to Red
};
```