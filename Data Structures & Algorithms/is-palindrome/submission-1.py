class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=[]
        for c in s.lower():
            if ((ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('0') <= ord(c) and ord(c) <= ord('9'))):
                ch.append(c)

        for i in range(len(ch)):
            if (ch[i]!=ch[len(ch)-i-1]) and (i<=len(s)/2):
                return False
        return True


