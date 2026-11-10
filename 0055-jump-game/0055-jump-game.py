class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0

        for i in range(len(nums)):

            # Check whether current index is reachable
            if i > max_reach:
                return False

            # Update maximum reachable index
            max_reach = max(max_reach, i + nums[i])

        return True