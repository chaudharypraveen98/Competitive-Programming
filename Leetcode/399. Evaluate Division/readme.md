# [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/description/)

## Approach
1.  If `x / y` is asked and either `x` or `y` are not in `equations`, we return -1, even if it is `x / x`.
2.  In Example 2, `"bc"` is a single variable, it is **NOT** `b * c`. Treat every string `equations[i][j]` as an atomic variable, not a product of some.

# Hint 1

One thing that you might have thought is that if we are given a/b\=n1​ and b/c\=n2​, then we can calculate a/c as (a/b)∗(b/c)\=n1​n2​. We can multiply or divide few given equations to cancel out some variables and generate new equations.  
Let's remove the option to divide by rearranging the equations in the form a\=n1​b and b\=n2​c. How can we generate a in terms of c now?

# Hint 2

To write a in terms of c, let's start with a\=n1​b. Put the value of b from b\=n2​c. New equation will be a\=n1​(n2​c)\=n1​n2​c\=n3​c, where n3​\=n1​n2​ is the answer for a/c.  
So, if we want to generate some variable x in terms of some other variable y, then we need some set of equations of the form  
x\=n1​x1​  
x1​\=n2​x2​  
x2​\=n3​x3​  
.  
.  
.  
xk​\=nk+1​y  
Using these equations we can start from x and reach y because there exists a **path** of variables \[x1​,x2​,...,xk​\] between them.  
And the final answer would become the product n1​n2​n3​...nk+1​.

# Hint 3

To get a path from x to y, we need to keep track of every equation of the form x\=ni​xi​ which starts with x and goes to some other variables xi​. We need this information for every given variable so that we can check if some variables put together will form a path or not.  
To do this, we can put them in a graph where each vertex will denote a variable and each edge will denote a relation of variables for equations a\=nb.  
For example, if a\=2b then graph will be  
![image.png](https://assets.leetcode.com/users/images/25e9b6d3-a1ad-4d0c-aef1-0a9b31223ad4_1684590881.5234437.png)  
Will this graph be directed or undirected? If a\=2b then is b\=2a?

# Hint 4

We need to make a directed graph for equations a\=nb. But what if we want to calculate b in terms of a? If a\=nb is an equation, then b\=(1/n)a is also another equation by which we can get b in terms of a.  
For example, if a\=2b, then graph will have 2 directed edges as  
![image.png](https://assets.leetcode.com/users/images/e1698aa9-a464-4685-b35e-9846e9fdc776_1684590750.7325034.png)

# Hint 5

Let's make graph for Example 2:

```sql
equations = [["a","b"],["b","c"],["bc","cd"]]
values    = [ 1.5,      2.5,      5.0]
```

The equations are a\=1.5b, b\=2.5c, bc\=5.0cd. (bc is just another different variable it is **NOT** equal to b∗c)  
The graph will be:  
![image.png](https://assets.leetcode.com/users/images/e067d848-dba4-47aa-a1da-aa2158fddcf5_1684590679.972568.png)

Now, calculate for given queries

```javascript
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
```

1.  Calculate a in terms of c as a\=1.5b\=1.5(2.5c)\=3.75c
2.  Calculate c in terms of b as c\=0.4b
3.  Calculate bc in terms of cd as bc\=5cd
4.  Calculate cd in terms of bc as cd\=0.2bc

# Hint 6

Can we calculate a in terms of bc? No, there is no path of variables between them.  
Calculating some variable x in terms of some other variable y is same as finding a valid path between x and y, where the final answer of x/y will be the product of weights of edges ni​'s that are present in the path.

# Hint 7

Make the graph. For every equation a\=nb, add two edges `a --n--> b` and `a <--1/n-- b`.  
For each query \[c,d\], check if such nodes even exists in the graph or not. If they don't even exist, there is no path, return `-1` (Like in Example 1, `x` does not exists so return `-1` even if we just wanted `x / x`).  
If both c and d exists in the graph, traverse the graph to get a path between them, maintaining cost of path as product of weights of edges traversed. If path is found return the product, and if not, then `-1`.

Upvote if helps!