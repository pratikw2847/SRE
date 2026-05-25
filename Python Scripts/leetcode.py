class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        sum = 0
        for i in range(0,length):
            if s[i] == "I":
                sum = sum + 1
            elif s[i] == "V":
                sum = sum + 5
            elif s[i] == "X":
                sum = sum + 10
            elif s[i] == "L":
                sum = sum + 50
            elif s[i] == "C":
                sum = sum + 100
            elif s[i] == "D":
                sum = sum + 500
            elif s[i] == "M":
                sum = sum + 1000
            else: print("Invalid Character")

        return sum