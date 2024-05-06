## Tower of Hanoi


Problem Link-> [https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1](https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1)

### Approach (IBH - recursion)
1. solve(n,s,d,aux)
2. starting with n-1 `solve(n-1,s,h,d)`. why ? Because if we move `n-1` disks to destination or `d` rod then we can't put `nth` disk on top on `n-1` disks in `d` rod.
3. Once `n-1` disks are moved to helper or `h` rod. Now move the `nth` plate to destination.
4. Once nth is moved to `d`. Move all the `n-1` disks from `h` to `d`
5. Hurray done