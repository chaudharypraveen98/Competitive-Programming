def kmp(haystack, needle):
    lps = [0]*len(needle)
    i, prevLPS = 1, 0

    while i < len(needle):
        if needle[prevLPS] == needle[i]:
            lps[i] = prevLPS+1
            i += 1
            prevLPS += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS-1]

        i, j = 0, 0
        while i < len(haystack):
            if (haystack[i] == needle[j]):
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]

            if j >= len(needle):
                return i-len(needle)
        return -1


if __name__ == "__main__":
    print(kmp("AAAABAAAAABBBAAAAB", "ABABD"))
