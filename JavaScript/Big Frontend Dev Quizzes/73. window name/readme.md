## [73. window name](https://bigfrontend.dev/quiz/window-name)

### Approach
- The Window.name property gets/sets the name of the window's browsing context.
```
var name = {}; // this is converted using toString() 
console.log(name) // [object Object]
```

- name is a special case such that when you are using the variable named name in the global scope it is treated as window.name In Google Chrome, window.name gets the value as a string.