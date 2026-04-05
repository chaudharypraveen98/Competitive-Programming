## [Describe the difference between `<script>`, `<script async>` and `<script defer>`](https://www.greatfrontend.com/interviews/study/gfe75/questions/quiz/describe-the-difference-between-script-async-and-script-defer)



| Feature          | &lt;script&gt;         | &lt;script async&gt;     | &lt;script defer&gt;     |
|------------------|------------------------|--------------------------|--------------------------|
| Parsing behavior | Blocks HTML parsing    | Runs parallel to parsing | Runs parallel to parsing |
| Execution order  | In order of appearance | Not guaranteed           | In order of appearance   |
| DOM dependency   | No                     | No                       | Yes (waits for DOM)      |
