class Solution:
    def reverseBits(self, n: int) -> int:
        binN = bin(n)[2:]
        while len(binN) < 32:
            binN = '0' + binN

        return int('0b' + binN[::-1], 2)