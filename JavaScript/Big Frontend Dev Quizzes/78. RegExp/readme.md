## [78. RegExp](https://bigfrontend.dev/quiz/RegExp)

### Approach
Intuitively, it seems that output should be ["a","b","c"] since these items match the regular expression.

But when a regex has the global flag set, test() will advance the lastIndex of the regex. lastIndex is a property of RegExp that specifies the index at which to start the next match.

Basically,

As long as test() returns true, lastIndex will not reset—even when testing a different string!
When test() returns false, the calling regex's lastIndex property will reset to 0.
/^[a-z]$/gi 👉🏻 Any character from character set [a-z], g means global flag for multiple matches, i means character insensitive same as [a-zA-Z]

So the loop effectively becomes,
```
regExp.test('a') // true and it sets lastIndex = 1
regExp.test('b') // false as the lastIndex i.e. staring point is not 0, lastIndex resets
regExp.test('c') // true as lastIndex is 0 and regex satisfies
regExp.test('1') // false
```