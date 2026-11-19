class Solution:
    def subsets(self, nums):
        result = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                result.append(curr.copy())
                return

            # Include current element
            curr.append(nums[i])
            backtrack(i + 1)

            # Exclude current element
            curr.pop()
            backtrack(i + 1)

        backtrack(0)
        return result