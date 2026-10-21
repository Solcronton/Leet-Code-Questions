
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cand = None
        c = 0
        for i in nums:
            if c == 0:
                cand = i

            if i == cand:
                c += 1
            else:
                c -= 1

        return cand
