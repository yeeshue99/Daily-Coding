from collections import defaultdict
class Solution(object):
    def CanSpell(self, mag, word):
        numLetters = defaultdict(int)
        for letter in mag:
            if letter in numLetters:
                numLetters[letter] = numLetters[letter] + 1
            else:
                numLetters[letter] = 1

        for letter in word:
            if letter in numLetters and numLetters[letter] > 0:
                numLetters[letter] -= 1
            else:
                return False

        return True


print(Solution().CanSpell(["a", "b", "c", "d", "e", "f"], "bed"))
# True

print(Solution().CanSpell(["a", "b", "c", "d", "e", "f"], "cat"))
# False
