class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        see = set()
        left = right = 0
        max_len = 0

        while right < len(s):

            while s[right] in see:
                see.remove(s[left])
                left += 1

            see.add(s[right])

            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len

            

