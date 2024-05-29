# 63.35% Runtime
# 99.12% Memory

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        for index in range(len(haystack) - len(needle) + 1):
            needle_index = 0
            match = True
            
            for check_index in range(len(needle)):
                if needle[needle_index] != haystack[check_index + index]:
                    match = False
                    break
                needle_index += 1
            if match:
                return index
        return -1