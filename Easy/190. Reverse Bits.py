class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]
        num = "0"*(32-len(num)) + num
        reverse = 0
        for i in range(len(num)):
            print(num[i])
            reverse += int(num[i]) * (2 ** i)
        return reverse

print(Solution().reverseBits(43261596))