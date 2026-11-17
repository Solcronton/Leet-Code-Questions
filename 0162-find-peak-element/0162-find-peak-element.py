class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        n=len(nums)

        if n==1 :
            return 0
        elif n==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        elif n==3:
            if nums[1]>nums[0] and nums[1]>nums[2]:
                return 1
        if n%2==1:
            if nums[n//2]>nums[(n//2)-1] and nums[n//2]>nums[(n//2)+1]:
                return n//2

        for i in range(1,n//2):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
            if nums[n-i-1]>nums[n-i] and nums[n-i-1]>nums[n-i-2]:
                return n-i-1
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        
                