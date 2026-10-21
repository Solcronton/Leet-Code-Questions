class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits.reverse()
        for i in range(len(digits)):
            if  i==0:
                digits[i]+=1
            if digits[i]==10:
                digits[i]=0
                if i + 1 < len(digits):
                    digits[i + 1] += 1
                else:
                    digits.append(1)            
            
        digits.reverse()
        return digits

        