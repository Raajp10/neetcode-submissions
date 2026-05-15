class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        post=[1]
        x=1
        y=1
        answer=nums

        for i in range(1,len(nums)):
            x*=nums[i-1]
            pre.append(x)
            
        x=1
        for i in range(len(nums)-1,0,-1):
            x*=nums[i]
            post.insert(0,x)

        print(pre,post,answer)
        for i in range(len(nums)):
            answer[i]=pre[i]* post[i]
        
        return answer


