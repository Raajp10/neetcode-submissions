class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [] 
        post = []
        mx = 0
        for i in range(len(height)):
            if(height[i]>mx):
                mx=height[i]
            pre.append(mx)

        mx = 0
        for i in range(len(height)-1,-1,-1):
            if(height[i]>mx):
                mx=height[i]
            post.append(mx)
            
        
        return sum([min(pre[i],post[len(post)-i-1])- height[i] for i in range(len(height))])
    