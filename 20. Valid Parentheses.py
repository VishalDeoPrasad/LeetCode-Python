class Solution(object):
    def isValid(self, s):
        stack = []     #    
        for c in s:      
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:  #if there is clossing parameter and list is empty then nothing to compair
                    return False
                temp = stack[-1]
                if (temp == '(' and c == ')') or (temp == '{' and c == '}') or (temp == '[' and c == ']'): #find combination opening anc closing
                    stack.pop()
                else:
                    return False
        return True

s = Solution()
testcase1 = '[()][{()}]'
testcase2 = "())"
testcase3 = ']()'
print(s.isValid(testcase1))