class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        for i in range(32):
            power = 2 ** (31 - i)
            if n >= power:
                n -= power
                bit_count += 1
        return bit_count
    
print(Solution().hammingWeight(11))