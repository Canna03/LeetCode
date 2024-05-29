# 99.09% Runtime
# 80.45% Memory

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        def steps_to_n(n: int) -> int:
            if n in cache:
                return cache[n]
            steps = steps_to_n(n - 2) + steps_to_n(n - 1)
            cache[n] = steps
            return steps
        return steps_to_n(n)

test = Solution()
print(test.climbStairs(45))

# 83.36% Runtime
# 80.45% Memory

# Fibonacci Sequence Solution
class Solution2:
    def climbStairs(self, n: int) -> int:
        num1 = 0
        num2 = 1
        for _ in range(n):
            num1, num2 = num2, num1 + num2
        return num2

test2 = Solution2()
print(test2.climbStairs(45))