class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre=[1]
        # answer=[1]*len(nums)
        # x=1
    
        # # prefix = [1 , 1*nums[0] , pre[1]*nums[1] ... ]
        # for i in range(1,len(nums)):
        #     x*=nums[i-1]
        #     pre.append(x)
            
        # x=1
        # # postfix = [... ,len(nums)-1 * 1 ,1]
        # for i in range(len(nums)-1,0,-1):
        #     x*=nums[i]
        #     post[len(nums)-1-i]=x

        # # answer = prefix* postfix        
        # return [pre[i]* post[i] for i in range(len(nums))]

        n = len(nums)

        res = [1] * n

        # Step 1: build prefix products in res
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Step 2: multiply by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

