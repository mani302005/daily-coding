class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        l = len(s)
        count = 0

        while i < l - 2:
            j = i + 2
            while j < l:
                sub = s[i:j+1]

                if 'a' in sub and 'b' in sub and 'c' in sub:
                    count += 1

                j += 1
            i += 1

        return count