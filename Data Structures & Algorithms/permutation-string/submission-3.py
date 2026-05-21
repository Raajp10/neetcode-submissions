class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if (len(s2)<len(s1)):
        #     return False
            
        # pos = []

        # for i in range(len(s2)):
        #     if s1[0] == s2[i]:
        #         pos.append(i)
        
        # if pos == []:
        #     return False
            
        # for i in range(len(pos)):
            
        #     left = pos[i] - len(s1) + 1
        #     right = pos[i] 
            
        #     while(right < len(s2)):
               
        #         if sorted(s2[left:right+1]) == sorted(s1):
        #             return True
        #         else:
        #             left+=1
        #             right+=1
        #     return False

        #using sliding window 

        if len(s1) > len(s2):
            return False

        s1Freq = [0]*26
        s2Freq = [0]*26
        s1_len = len(s1)

        for c in s1:
            s1Freq[ord(c)-ord('a')]+=1

        for i in range(s1_len):
            s2Freq[ord(s2[i])-ord('a')]+=1

        if s1Freq == s2Freq:
            return True

        for i in range(s1_len,len(s2)):
            s2Freq[ord(s2[i])-ord('a')]+=1
            s2Freq[ord(s2[i-s1_len])-ord('a')]-=1

            if s1Freq == s2Freq:
                return True

        return False
            


        
            


        
            

        