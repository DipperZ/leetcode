class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        #容积等于长乘宽
        # area = (j-i)*min(nums[i],nums[j])
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right-left)* min(height[left],height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxarea = max(area,maxarea)
        return maxarea
if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))