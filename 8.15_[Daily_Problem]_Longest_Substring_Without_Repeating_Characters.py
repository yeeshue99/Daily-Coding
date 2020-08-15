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


timer = Timer()
timerList = []
for _ in range(10000):
    timer.Start()
    print(Solution().lengthOfLongestSubstring("eeydgwdykpv"))
    timerList.append(timer.Stop())
print("done")
# timer.Average(timerList)
# 10
