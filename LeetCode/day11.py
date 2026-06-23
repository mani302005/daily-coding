from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        char_count = defaultdict(int)
        substr_count = defaultdict(int)

        left = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            if right - left + 1 > minSize:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            if right - left + 1 == minSize:
                if len(char_count) <= maxLetters:
                    substr = s[left:right + 1]
                    substr_count[substr] += 1

        return max(substr_count.values(), default=0)