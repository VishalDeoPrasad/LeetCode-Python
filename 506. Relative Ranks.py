class Solution(object):
    def findRelativeRanks(self, score):
        new_score = list(score)
        new_score.sort(reverse=True)
        rank = {}
        for i in range(len(new_score)):
            if i==0:
                rank[new_score[i]] = "Gold Medal"
            elif i==1:
                rank[new_score[i]] = "Silver Medal"
            elif i==2:
                rank[new_score[i]] = "Bronze Medal"
            else:
                rank[new_score[i]] = str(i+1)

        ans = [rank[s] for s in score]
        return ans
    
score = [5,4,3,2,1]
print(Solution().findRelativeRanks(score))