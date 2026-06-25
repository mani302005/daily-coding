class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        arr = [-1, -1]
        ind = -1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                ind = m
                break
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        if ind == -1:
            return arr

        l = ind
        r = ind

        while l > 0 and nums[l - 1] == target:
            l -= 1

        while r < len(nums) - 1 and nums[r + 1] == target:
            r += 1

        arr[0] = l
        arr[1] = r

        return arr