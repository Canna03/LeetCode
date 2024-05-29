# 82.57% Runtime
# 96.17% Memory

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ["I", "V", "X", "L", "C", "D", "M"]
        value = [1, 5, 10, 50, 100, 500, 1000]
        
        highest = 6
        total = 0
        
        for i in range(len(s)):
            letter = symbol.index(s[i])
            
            if letter > highest + 1:
                total += value[highest] * 8
            elif highest < letter:
                total += value[highest] * 3
            else:
                highest = letter
                total += value[highest]
                
        return total