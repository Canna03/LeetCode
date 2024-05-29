# 69.05% Runtime
# 42.12% Memory

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        smallest_length = len(strs[0])
        for word in strs:
            if len(word) < smallest_length:
                smallest_length = len(word)
        
        for letter in range(smallest_length):
            for word in strs[1:]:
                if word[letter] != strs[0][letter]:
                    return prefix
            prefix += strs[0][letter]
        return prefix
            
        
        

test = Solution()
print(test.longestCommonPrefix(["ab","a"]))