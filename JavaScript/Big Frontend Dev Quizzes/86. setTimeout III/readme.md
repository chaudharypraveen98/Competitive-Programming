## [86. setTimeout III](https://bigfrontend.dev/quiz/setTimeout-III)

### Approach
1. Here, the func is changed inside the first setimeout but since this is part of the callback it will not execute until the first setTimeout is invoked. That is why, the original func is passed as a reference to the second timeout which eventually gets invoked after 100ms logging 1
2. use event loop concept