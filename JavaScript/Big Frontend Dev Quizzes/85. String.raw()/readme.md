## [85. String.raw()](https://bigfrontend.dev/quiz/String-raw)

### Approach
The static String.raw() method is a tag function of template literals. It's used to get the raw string form of template literals, that is, substitutions (e.g. ${foo}) are processed, but escapes (e.g. \n) are not. Note that it works just like the default template function and performs string concatenation. The important difference is that it'll not escape characters.

```
console.log(String.raw`BFE\n.${'dev'}`) // "BFE\n.dev"
console.log(String.raw({raw: 'BFE'}, 'd', 'e','v')); // "BdFeE"

```

String.raw() works like an interweaving function. The first argument is an object with a raw property whose value is an iterable(could be a string or an array) representing the separated strings in the template literal. The rest of the arguments are the substitutions. Extra substitutions are ignored

For example, 'test' is treated as ['t', 'e', 's', 't']. The following is equivalent to `t${0}e${1}s${2}t`:

```
// using array
String.raw({ raw: [0,2,4] }, 1, 3, 5, 6, 7) // "01234"
// using string
String.raw({ raw: '024' }, 1, 3, 5, 6, 7) // "01234"

```