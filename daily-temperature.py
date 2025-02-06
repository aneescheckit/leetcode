class Solution:
    def __init__(self):
        self.currentZeroAt = 0

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nextHighTemperature = []
        result = []
        for i in range(len(temperatures) -1, -1, -1):
            currentTemperature = temperatures[i]
            
            while len(nextHighTemperature) != 0:
                if temperatures[nextHighTemperature[len(nextHighTemperature) - 1]] > currentTemperature:
                    result.append(nextHighTemperature[len(nextHighTemperature) - 1] - i)
                    nextHighTemperature.append(i)
                    break
                else:
                    nextHighTemperature.pop()
            
            if len(nextHighTemperature) == 0:
                result.append(0)
                nextHighTemperature.append(i)

        return result[::-1]
