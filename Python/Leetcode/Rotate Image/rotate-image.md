* Observe the pattern

| 1 | 2 | 3 |
|:-:|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

=>

| 7 | 4 | 1 |
|:-:|---|---|
| 8 | 5 | 2 |
| 9 | 6 | 3 |

* Read the constraints
  * in place computation
  * we need to store previous value if we are going to overwrite. It's 90 degree rotate not traverse that we can swap
  * Try to think out of box


* Try to extend the box to store value and it can be easily done using list append operation.

start the loop in reverse and utilize the append operation.

we can start filling the table from column 4.

| 1 | 2 | 3 | 4 | . | . |
|---|---|---|---|:-:|---|
| 4 | 5 | 6 | 5 | . | . |
| 7 | 8 | 9 | . | . | . |
