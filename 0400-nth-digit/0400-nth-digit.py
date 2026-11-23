
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        start = 1
        count = 9

        while n > count:
            n -= count
            digits += 1
            start *= 10
            count = 9 * start * digits
            
        number = start + (n - 1) // digits
        index = (n - 1) % digits
        return int(str(number)[index])
