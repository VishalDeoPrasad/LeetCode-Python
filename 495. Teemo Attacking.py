class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        total = 0
        for i in range(1, len(timeSeries)):
            
            
            if timeSeries[i]-timeSeries[i-1] == duration:
                total += duration
            else:
                total += timeSeries[i]-timeSeries[i-1]

        return total+duration

print(Solution().findPoisonedDuration([1,2,3,4,5,6,7,8,9], 1))