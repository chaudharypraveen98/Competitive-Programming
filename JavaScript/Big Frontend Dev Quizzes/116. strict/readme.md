## [116. strict](https://bigfrontend.dev/quiz/strict)

### Approach
'use strict' declaration executes your code in strict mode.

It usually forces stricter rules which allows writing safer code. One of the rule state

Undeclared variable is not allowed.
You can apply 'use strict' to functions.

```
function a() {
  'use strict' // initiates function level strict mode
  dev = 'BFE' // an undeclared variable 'dev' is being assigned a value. Not allowed. Error <---
  console.log(dev)
}

a()
```

Side note:

To execute code in strict mode, 'use strict' must be the first line of code in function.
'strict mode' in block declarations {} has no impact