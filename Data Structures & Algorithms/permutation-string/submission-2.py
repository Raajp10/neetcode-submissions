class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2)<len(s1)):
            return False
            
        pos = []
        for i in range(len(s2)):
            if s1[0] == s2[i]:
                pos.append(i)
        
        if pos == []:
            return False
            
        for i in range(len(pos)):
            
            left = pos[i] - len(s1) + 1
            right = pos[i] 
            
            while(right < len(s2)):
               
                if sorted(s2[left:right+1]) == sorted(s1):
                    return True
                else:
                    left+=1
                    right+=1
            return False
            


        
            

        