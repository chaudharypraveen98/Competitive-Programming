## [getElementsByClassName](https://www.greatfrontend.com/interviews/study/gfe75/questions/javascript/get-elements-by-class-name)

### Approach
1. `.filter(Boolean)` - It’s a clever JavaScript shortcut that relies on two core concepts: Function References and Truthy/Falsy values.
   The Function Reference
   Normally, we write .filter() with an arrow function like this:
   array.filter(item => Boolean(item))

   In JavaScript, if a function takes exactly one argument, you can pass the function name directly. This is called point-free style.
   So, .filter(Boolean) literally tells JavaScript: "Take every item in the array and pass it into the Boolean() constructor."
2. use classList and early exit if `length===0`