"""#68ms 13.9MB
class Solution:
    def lengthOfLongestSubstring(self, s):
        if(len(s) == 0):
            return 0
        if len(set(s)) <= 1:
            return 1
        else:
            currentLetters = defaultdict(int)
            i = 0
            length = 1
            currentLetters[s[i]] = 1
            for j in range(1, len(s)):
                if currentLetters[s[j]] == 0:
                    currentLetters[s[j]] = 1
                    if j - i > length:
                        length = j - i
                else:
                    newStart = s.find(s[j], i)
                    for k in s[i:newStart]:
                        currentLetters[k] = 0
                    i = newStart + 1
            return length + 1"""

"""#56ms 13.8MB
class Solution:
    def lengthOfLongestSubstring(self, s):
        if(len(s) == 0):
            return 0
        if len(set(s)) <= 1:
            return 1
        else:
            currentLetters = set()
            i = 0
            length = 1
            currentLetters.add(s[i])
            for j in range(1, len(s)):
                if not s[j] in currentLetters:
                    currentLetters.add(s[j])
                    if j - i > length:
                        length = j - i
                else:
                    newStart = s.find(s[j], i)
                    for k in s[i:newStart]:
                        currentLetters.discard(k)
                    i = newStart + 1
            return length + 1"""

from Timer import *


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        if len(set(s)) <= 1:
            return 1
        else:
            currentLetters = set()
            i = 0
            length = 1
            currentLetters.add(s[i])
            for j in range(1, len(s)):
                if not s[j] in currentLetters:
                    currentLetters.add(s[j])
                    if j - i > length:
                        length = j - i
                else:
                    newStart = s.find(s[j], i)
                    for k in s[i:newStart]:
                        currentLetters.discard(k)
                    i = newStart + 1
            return length + 1

    def longestUniqueSubsttr(self, string):

        # Creating a set to store the last positions of occurrence
        seen = {}
        maximum_length = 0

        # starting the inital point of window to index 0
        start = 0

        for end in range(len(string)):

            # Checking if we have already seen the element or not
            if string[end] in seen:

                # If we have seen the number, move the start pointer
                # to position after the last occurrence
                start = max(start, seen[string[end]] + 1)

            # Updating the last seen value of the character
            seen[string[end]] = end
            maximum_length = max(maximum_length, end - start + 1)
        return maximum_length


timer = Timer()
s = "eeydgwdykpveeydgwdykpveeydgwdykpveeydgwdykpveeydgwdykpveeydgwdykpveeydgwdykpveeydgwdykpveeydgwdykpveeydgwdykpv"

prob1 = timer.CalculateTime(Solution().lengthOfLongestSubstring, s)
# timer.Average(timerList)
# 10

prob2 = timer.CalculateTime(Solution().longestUniqueSubsttr, s)

print(f"Code 1: {prob1[0]} s,\n\t\t{prob1[1]}")
print(f"Code 2: {prob2[0]} ms,\n\t\t{prob2[1]}")
{}.
