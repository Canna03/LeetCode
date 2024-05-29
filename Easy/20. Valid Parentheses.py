# 90.55% Runtime
# 97.15% Memory

class Solution:
    def isValid(self, s: str) -> bool:
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        
        if len(s) % 2 != 0:
            return False
        
        parentheses = [""] * (len(s) // 2)
        
        pointer = 0
        
        for character in s:
            if character in left:
                if pointer >= len(parentheses):
                    return False
                parentheses[pointer] = character
                pointer += 1
            else:
                if pointer == 0:
                    return False
                pointer -= 1
                if right.index(character) == left.index(parentheses[pointer]):
                    parentheses[pointer] = ""
                else:
                    return False
        return True if pointer == 0 else False
    
test = Solution()
print(test.isValid("(("))