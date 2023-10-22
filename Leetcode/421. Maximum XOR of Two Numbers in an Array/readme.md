    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

Build the answer bit by bit from left to right (highest bit to lowest bit). Let's say we already know the largest first seven bits we can create. How to find the largest first eight bits we can create? Well it's that maximal seven-bits prefix followed by 0 or 1. Append 0 and then try to create the 1 one (i.e., `answer ^ 1`) from two eight-bits prefixes from `nums`. If we can, then change that 0 to 1.

Bit more explanation: `answer^1 ^ p in prefixes` means there's a prefix `q` in `prefixes` such that `answer^1 ^ p == q`. Which means `p ^ q == answer ^ 1`. So there are two prefixes (`p` and `q`) whose xor is `answer ^ 1`.

----
Additional explaination

I was shocked when I finally understand  
`answer += any(answer^1 ^ p in prefixes for p in prefixes)`  
Need to make a note for my future self.

The key idea is just build the maximal answer bit by bit, so that we want to add a '1' to every bit, but without changing the previous bits.  
By using XOR, how do we get `1`: just find two numbers, one has a `1` on this bit, the other has `0` (or they are opposite on this bit).  
How do we guarantee that these two numbers are exactly the same two who construct the previous part of this answer? If we denote the two numbers as `a` and `b`, then the previous answer shall be `a^b`. We also know `a` and `b` should exist in the set `prefix`, and `a^b^a=b`. The next part is fairly simple: using just try `answer ^ a` for all `a` in `prefix`, if the result still exists in `prefix`, then the result must be `b`.

So actually this `answer^1^p` test two things:

1.  find the two elements in `nums` that constructs the previous answer
2.  check this two elements have opposite bits at current position

**key idea:**   `answer += any(answer^1 ^ p in prefixes for p in prefixes)`  
if `(answer^1) XOR p` matches `Z` in `prefixes`, then `p XOR Z` matches `(answer^1)`, which is what I am looking for. `p` and `Z` are both elements in the prefix set.