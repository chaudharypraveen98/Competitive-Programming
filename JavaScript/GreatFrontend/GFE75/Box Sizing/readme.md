## [What does `* { box-sizing: border-box; }` do?](https://www.greatfrontend.com/interviews/study/gfe75/questions/quiz/what-does-box-sizing-border-box-do-what-are-its-advantages)

### What's the difference?
By default, elements have box-sizing: content-box applied, and only the content size is being accounted for if an element has height and width specified. box-sizing: border-box changes how the width and height of elements are being calculated, border and padding are also being included in the calculation. The height of an element is now calculated by the content's height + vertical padding + vertical border width. The width of an element is now calculated by the content's width + horizontal padding + horizontal border width.

The following table indicates whether the property is included in the element's calculation of height and width when it has the respective box-sizing:

| Property | box-sizing: content-box (default) | box-sizing: border-box |
|----------|-----------------------------------|------------------------|
| content  | Yes                               | Yes                    |
| padding  | No                                | Yes                    |
| border   | No                                | Yes                    |
| margin   | No                                | No                     |
