# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

from collections import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # funtion to calculate the euclidian distance from the origin
        def dist(x,y):
            return sqrt(x**2 + y**2)
            # the complete equation would be:
            # sqrt((0-x)**2 + (0-y)**2)
            # but the 0 from the origin do make a difference if they are left out

        heap = []
        for x,y in points:
            d = dist(x,y)
            #If the size of the heap is less than k, it adds a new element to the heap. 
            #The elements are tuples of the form (-d, x, y), 
            #where d is the distance (negated to simulate a max heap), and (x, y) are the coordinates of the point.
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            #If the size of the heap is already equal to k, 
            #it pushes a new element onto the heap and simultaneously pops off the smallest element.
            #This ensures that the heap maintains the k-smallest elements.
            else:
                heapq.heappushpop(heap, (-d, x, y))


        return [(x,y) for _,x,y in heap]
    
