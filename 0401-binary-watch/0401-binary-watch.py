
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:

        result = []

        for hour in range(12):
            for minute in range(60):

                count = bin(hour).count('1') + bin(minute).count('1')

                if count == turnedOn:
                    time = str(hour) + ":" + str(minute).zfill(2)
                    result.append(time)

        return result
