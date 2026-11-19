class Solution:
    def subsets(self, nums):
        result = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                result.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(i + 1)

            curr.pop()
            backtrack(i + 1)

        backtrack(0)
        return result