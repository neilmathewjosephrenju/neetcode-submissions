from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:

            # Calculate the current area
            width = right - left
            currHeight = min(height[left], height[right])
            area = width * currHeight

            # Update the maximum area
            maxArea = max(maxArea, area)

            # Move the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea