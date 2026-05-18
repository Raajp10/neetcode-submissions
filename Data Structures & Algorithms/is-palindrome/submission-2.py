class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ch=[]
        # for c in s.lower():
        #     if ((ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('0') <= ord(c) and ord(c) <= ord('9'))):
        #         ch.append(c)

        # for i in range(len(ch)):
        #     if (ch[i]!=ch[len(ch)-i-1]) and (i<=len(s)/2):
        #         return False
        # return True

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
            

