class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        #bruteforce
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                curr = (j-i) * min(heights[i],heights[j])
                if (curr > maxi):
                    maxi=curr
        return  maxi
            

            
        