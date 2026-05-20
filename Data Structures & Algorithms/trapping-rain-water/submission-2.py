class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        pre = [0] * n
        post = [0] * n

        mx = 0
        for i in range(n):
            mx = max(mx, height[i])
            pre[i] = mx

        mx = 0
        for i in range(n - 1, -1, -1):
            mx = max(mx, height[i])
            post[i] = mx

        return sum(min(pre[i], post[i]) - height[i] for i in range(n))