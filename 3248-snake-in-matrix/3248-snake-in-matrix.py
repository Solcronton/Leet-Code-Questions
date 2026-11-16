class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        r=0
        c=0
        for i in commands:
            if i == "RIGHT":
                c=c+1
            elif i == "LEFT":
                c=c-1
            elif i == "UP":
                r=r-1
            else:
                r=r+1
        f=(r*n)+c
        return f
                
        