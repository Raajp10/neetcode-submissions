class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        post = [0] * len(height)
        mx = 0

        for i in range(len(height)):
            if(height[i]>mx):
                mx=height[i]
            pre[i]=mx

        mx = 0
        for i in range(len(height)-1,-1,-1):
            if(height[i]>mx):
                mx=height[i]
            post[i]=mx
            
        
        return sum([min(pre[i],post[i])- height[i] for i in range(len(height))])
    