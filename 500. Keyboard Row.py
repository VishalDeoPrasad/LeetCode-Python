class Solution(object):
    def categoryDic(self):
        cat_dic = {}
        cat_no = 0
        for i in range(97, 123):
            if chr(i) in "qwertyuiop": cat_no = 1 
            elif chr(i) in "asdfghjkl": cat_no = 2
            elif chr(i) in "zxcvbnm": cat_no = 3
            cat_dic[chr(i)] = cat_no
        return cat_dic
    def findWords(self, words):
        cat_dic = self.categoryDic()
        ans = []
        for word in words:
            word_lower = word.lower()
            cnt = set()
            for ch in word_lower:
                cnt.add(cat_dic[ch])
            if len(cnt) == 1:
                ans.append(word)
        return ans
words = ["Hello","Alaska","Dad","Peace"]
print(Solution().findWords(words))