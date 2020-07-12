#Question 12 : Reverse bits

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2::]
        binary = '0'*(32 - len(binary)) + binary
        return int(binary[::-1],2)