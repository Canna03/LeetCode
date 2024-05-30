class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        characters = ''
        for chr in s:
            if chr in 'abcdefghijklmnopqrstuvwxyz0123456789':
                characters += chr
        if len(characters) % 2 == 0:
            return True if characters[0:len(characters) // 2] == characters[len(characters) : len(characters) // 2 - 1 : -1] else False
        return True if characters[0:len(characters) // 2] == characters[len(characters) : len(characters) // 2 : -1] else False
        
print(Solution().isPalindrome("raceacar"))
        
            