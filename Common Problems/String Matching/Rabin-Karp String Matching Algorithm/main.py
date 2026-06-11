def rabin_karp(text, pattern):
    MOD = 101
    BASE = 256
    m = len(pattern)

    h = pow(BASE, m - 1, MOD)

    def create_hash(s):
        hsh = 0
        for ch in s:
            hsh = (hsh * BASE + ord(ch)) % MOD
        return hsh

    def roll(old_hash, outgoing, incoming):
        return (
            (old_hash - ord(outgoing) * h) * BASE
            + ord(incoming)
        ) % MOD

    pattern_hash = create_hash(pattern)
    window_hash = None

    for start in range(len(text) - m + 1):
        if window_hash is None:
            window_hash = create_hash(text[:m])
        elif start > 0:
            window_hash = roll(
                window_hash,
                text[start - 1],
                text[start + m - 1]
            )

        if (
            window_hash == pattern_hash
            and text[start:start + m] == pattern
        ):
            return start

    return -1


print(rabin_karp("aabcdqaaabftghj", "aaab"))
