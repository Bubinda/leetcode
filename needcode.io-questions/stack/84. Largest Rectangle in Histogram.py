# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # we take track of the max area over all
        max_area = 0
        # we also save the length of the input
        n = len(heights)

        # we loop over the langth of the input
        for i in range(n):
            # if we have elements in our stack and the element of the current index of the input is smaler than the last element in our input
            while stack and heights[i] < heights[stack[-1]]:
                # we take out the last index of the stack and with it get the elemnt in the input as height (the input alsway stores integers that are representing the height of a bar)
                height = heights[stack.pop()]
                # the width of the rectangle is calculated by the current index of the loop if the stack is empty, otherwise we sutrack the last element in the stack from the current loop index
                width = i if not stack else i - stack[-1] - 1
                # then the new max area is saved
                max_area = max(max_area, height * width)
            # in the end of the loop we always append the current loop index
            stack.append(i)

        # if we ran over the whole input and the stack still contains elements we go through the whole process of area calculation until the stack is empty
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        # then in the end we return our max area of the whole input
        return max_area