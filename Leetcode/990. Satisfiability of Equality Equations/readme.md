## [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/description/)

### Approach
1. Use of Union Find.
2. First, place all == relationships into disjoint sets. Then, process the != relationships, for != ensure that the ultimate parents of the characters involved are not the same. If they are the same, it would contradict the == relationships.