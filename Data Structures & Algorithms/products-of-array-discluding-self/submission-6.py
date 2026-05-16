class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        post=[1]* len(nums)
        x=1
    
        # prefix = [1 , 1*nums[0] , pre[1]*nums[1] ... ]
        for i in range(1,len(nums)):
            x*=nums[i-1]
            pre.append(x)
            
        x=1
        # postfix = [... ,len(nums)-1 * 1 ,1]
        for i in range(len(nums)-1,0,-1):
            x*=nums[i]
            post[i-1]=x

        # answer = prefix* postfix        
        return [pre[i]* post[i] for i in range(len(nums))]


