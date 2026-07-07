class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        k = ""
        f = 0

        for i in s:
            if i != "0":
                k += i
                f += int(i)

        if k == "":
            return 0
        return int(k) * f    
m = Solution()
print(m.sumAndMultiply(1234))      