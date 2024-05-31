class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0
        for letter in columnTitle:
            column *= 26
            position = ord(letter) % 64
            column += position
        return column