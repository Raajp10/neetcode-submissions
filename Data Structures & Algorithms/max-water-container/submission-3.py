class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxi = 0
        # #bruteforce
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         curr = (j-i) * min(heights[i],heights[j])
        #         if (curr > maxi):
        #             maxi=curr
        # return  maxi

        max1 = 0
        left = 0
        right = len(heights)-1

        while(left < right):
            curr = abs(right-left) * min(heights[left],heights[right])
            if(curr > max1):
                max1=curr
            if(heights[left] < heights[right]):
                left+=1
            else:
                right-=1

        return max1




            

            
        