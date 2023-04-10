class Solution(object):
    def fizzBuzz(self, n):
        game = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                game.append("FizzBuzz")
            elif i%3 == 0:
                game.append("Fizz")
            elif i%5 == 0:
                game.append('Buzz')
            else:
                game.append(str(i))
        return game
 
print(Solution().fizzBuzz(5))