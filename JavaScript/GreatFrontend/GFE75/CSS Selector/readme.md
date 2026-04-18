## [Explain how a browser determines what elements match a CSS selector.](https://www.greatfrontend.com/interviews/study/gfe75/questions/quiz/explain-how-a-browser-determines-what-elements-match-a-css-selector)

### Approach
n reality, browsers evaluate CSS selectors from Right-to-Left.

Here is the easy breakdown of how it works and why.

1. The Key Selector (The "Right-most" Part)
The very last item in your CSS selector chain is called the Key Selector. This is where the browser starts.

Using div .header .title as an example:

The Key Selector is .title.

The browser doesn't start by looking at the whole page structure. It starts by looking for every element on the page that has the class .title.

2. The Detective Analogy
Imagine you are a detective trying to find a specific person in a giant city:

Left-to-Right (Inefficient): You try to find every single person in the city, then check if they live in the "North District," then check if they work in the "Blue Building." That is billions of unnecessary checks.

Right-to-Left (Efficient): You find the person whose name is "John Smith" (The Key Selector). Then, you look up to see if he lives in the "Blue Building." Then, you check if that building is in the "North District."


### Why do browsers do this? (Performance)
The goal is to stop as early as possible.