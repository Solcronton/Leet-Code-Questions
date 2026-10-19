class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lt=[]
        for i in nums:
            if i!=val:
                lt.append(i)
        nums[:]=lt
        return len(lt)
        
    

