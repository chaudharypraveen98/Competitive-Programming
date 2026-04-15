## [Explain your understanding of the box model and how you would tell the browser in CSS to render your layout in different box models.](https://www.greatfrontend.com/interviews/study/gfe75/questions/quiz/explain-your-understanding-of-the-box-model-and-how-you-would-tell-the-browser-in-css-to-render-your-layout-in-different-box-models)


### Things to focus
1. By default `(box-sizing: content-box)`, paddings and borders are not part of the width and height of an element.
2. `box-sizing: border-box`: The width and height will include the content, padding and border (but not the margin). 
3. Borders do not collapse or overlap with those of adjacent elements. Each element’s border is rendered individually.
4. Margins can collapse, but only vertically and only between block-level elements. Horizontal margins do not collapse. This means that if one block element has a bottom margin and the next has a top margin, only the larger of the two will be used. This behavior is independent of box-sizing and is the default in CSS.