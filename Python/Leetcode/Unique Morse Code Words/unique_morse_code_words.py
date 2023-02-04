class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morse_dict = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_trans = set()
        for word in words:
            temp_decoded=""
            for i in word:
                temp_decoded+=morse_dict[ord(i) - ord('a')]
            unique_trans.add(temp_decoded)
        return len(unique_trans)

item  = Solution()
print(item.uniqueMorseRepresentations(["gin","zen","gig","msg"]))