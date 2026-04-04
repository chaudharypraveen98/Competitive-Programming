## [What's the difference between a JavaScript variable that is: `null`, `undefined` or undeclared?](https://www.greatfrontend.com/interviews/study/gfe75/questions/quiz/whats-the-difference-between-a-variable-that-is-null-undefined-or-undeclared-how-would-you-go-about-checking-for-any-of-these-states)


| Trait                      | null                                                                     | undefined                                           | Undeclared                            |
|----------------------------|--------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------|
| Meaning                    | Explicitly set by the developer to indicate that a variable has no value | Variable has been declared but not assigned a value | Variable has not been declared at all |
| Type (via typeof operator) | 'object'                                                                 | 'undefined'                                         | 'undefined'                           |
| Equality Comparison        | null == undefined is true                                                | undefined == null is true                           | Throws a ReferenceError               |
