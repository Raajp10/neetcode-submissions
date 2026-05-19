class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nlog(n)
        nums=sorted(nums)
        answer=[]
        # n^2
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while(left < right):
                curr = nums[i] + nums[left] + nums[right]
                if(curr == 0):
                    x=[nums[i],nums[left],nums[right]]
                    right-=1
                    if x not in answer:
                        answer.append(x)
                elif (curr < 0):
                    left+=1
                else:
                    right-=1
        return answer