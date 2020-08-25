class Solution(object):
    def twoSum(self, nums, n):
        sums = {}
        ans = []
        for counter, number in enumerate(nums):
            if n - number in sums:
                return [sums[n - number], counter]
            else:
                sums[number] = counter
        return False


print(Solution().twoSum([2, 7, 11, 15], 18))
