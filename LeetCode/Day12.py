class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a = {}
        m = 0
        j = 0

        for i in range(len(fruits)):
            if fruits[i] in a:
                a[fruits[i]] += 1

            elif len(a) < 2:
                a[fruits[i]] = 1

            else:
                m = max(m, i - j)

                while len(a) == 2:
                    a[fruits[j]] -= 1

                    if a[fruits[j]] == 0:
                        del a[fruits[j]]

                    j += 1

                a[fruits[i]] = 1

        m = max(m, len(fruits) - j)
        return m