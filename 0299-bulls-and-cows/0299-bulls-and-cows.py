class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a=0
        b=0

        s=[0]*10
        g=[0]*10


        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                s[int(secret[i])] += 1
                g[int(guess[i])] += 1

        for i in range(10):
            b += min(s[i], g[i])

        return str(a) + "A" + str(b) + "B"
        