class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        if len(set(s)) == 1:
            return s
        longest = ""
        for i in range(len(s)):
            for j in range(len(s) + 1):
                string = s[i:j]
                if string == string[::-1] and j - i > len(longest):
                    longest = string
        return longest


# Test program
s = "babad"
print(str(Solution().longestPalindrome(s)))
# racecar

from Timer import Timer

timer = Timer()
timer.CalculateTime(Solution().longestPalindrome, s)
