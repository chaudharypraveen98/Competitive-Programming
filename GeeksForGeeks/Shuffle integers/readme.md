Link -> [Shuffle integers](https://www.geeksforgeeks.org/problems/shuffle-integers2401/1)

## Approach
We try to save two values into single value.

### Explanation
 `(arr[end] % mx) * mx + (arr[i] % mx)`:
- `mx` value greater than `1 ≤ arri ≤ 10**3` in power of `2` i.e `10**4`.
- **`arr[end] % mx`**: This operation extracts the last 4 digits (or the remainder when dividing by `mx`) as our max value range in question is `1 ≤ arri ≤ 10**3`, which is the value at index `end`.
- **`(arr[end] % mx) * mx`**: Multiplying this by `mx` shifts it left by 4 digits. This allows the original value of `arr[i]` to be stored without overwriting it.
- **`+ (arr[i] % mx)`**: This adds the original value of `arr[i]`, which has already been shifted to make space for the new value.


Let's use the array `arr = [1, 2, 3, 4, 5, 6]` to illustrate how the expression `(arr[end] % mx) * mx + (arr[i] % mx)` works step by step.

### Initial Setup:
- **`arr = [1, 2, 3, 4, 5, 6]`**
- **`n = len(arr) = 6`**
- **`mx = 10000`**
- **`start = 1`**, **`end = n // 2 = 3`**

### Loop Iterations:

#### Iteration 1 (`i = 1`, odd index):
- **`arr[i] = arr[1] = 2`**
- **`arr[end] = arr[3] = 4`**

Let's apply the expression:

1. **`arr[end] % mx`**:
   - `arr[3] % mx = 4 % 10000 = 4`

2. **`(arr[end] % mx) * mx`**:
   - `4 * 10000 = 40000`

3. **`arr[i] % mx`**:
   - `arr[1] % mx = 2 % 10000 = 2`

4. **Combining**:
   - `40000 + 2 = 40002`

Now, `arr[1]` is temporarily set to `40002`.

**Array state:** `[1, 40002, 3, 4, 5, 6]`

**Update `end`:** `end = 4`



### Why is this done?
- This technique allows the original and new values to be combined temporarily in a single array element. The multiplication by `mx` shifts the new value into the higher digits, leaving the original value in the lower digits. 
- Later, by dividing by `mx`, the original values are removed, leaving only the shuffled new values.

This approach ensures the original array elements aren't lost before the final assignment is made in the second loop.
