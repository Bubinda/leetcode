# Given an array of integers temperatures represents the daily temperatures, 
#return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
#If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        # we keep track of the temperatur chenges with an index array
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # if our stack is not empty and we see a temperatur at the top of our stack that is lower than the current temperautr in our input list
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # then we pop the lower temperatur
                index = stack.pop()
                # and keep track of the days in difference since the lower temperatur in our result list
                result[index] = i - index
            # then we append the current temperatur index
            stack.append(i)

        return result



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and stk[-1][1] < temperatures[i]:
                stk_i, stk_temp = stk.pop()
                answer[stk_i] = i - stk_i
            
            stk.append((i,temperatures[i]))

        return answer