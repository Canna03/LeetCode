class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        people = 0
        for c in s:
            if c == 'E':
                people += 1
            else:
                people -= 1
            chairs = max(chairs, people)
        return chairs