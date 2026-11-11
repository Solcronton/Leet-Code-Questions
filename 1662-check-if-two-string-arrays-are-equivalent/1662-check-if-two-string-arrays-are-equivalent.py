class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        k="".join(word1)
        l="".join(word2)
        if k==l:
            return 1==1
        else:
            return 1==0