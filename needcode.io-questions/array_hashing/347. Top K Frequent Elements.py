# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        # first we build up a hasmap with the frequency count of all the elements in the input
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        # the main part of the function is the upput list
        # in this list comprehansion the key elements i[0] of the hashmap are added
        # the elments of the hashmap are sorted by a lambda function where the key to sort are the values x[1] which are the items (frequencies of the elements of the input)
        # thosre sorting is done in reverse so the elements with the highest values are on top 
        # in the end we slice the list and taking only the first elment up to the index k
        return [i[0] for i in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]]
    


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get((i), 0) + 1
            
        sorted_list = [i[0] for i in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)][:k]
        return sorted_list
    

    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            # for this solution we build up a frequency list
            freq = [[] for i in range(len(nums) + 1)]

            # the hasmap is filled up with the frequency of the elemnts also the list is filled up
            for n in nums:
                count[n] = 1 + count.get(n, 0)
            # the list is filled by the index of the elment and the corresponding count
            for n,c in count.items():
                freq[c].append(n)

            res = []
            # in the end we walk over the len of our frequency count in reverse
            for i in range(len(freq)-1, 0, -1):
                # we walk over the frequency list
                for n in freq[i]:
                    # we append each element of the list to the result
                    res.append(freq[i])
                    # if the lenght of the result is equl to k we return the result list
                    if len(res) == k:
                        return res



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * n

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
            
        ret = []
        for i in range(n,0,-1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                return ret






import heapq
from collections import Counter

# using a heap (min heap)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))

        return [t[1] for t in heap]




# using a heap (min heap)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        return [heapq.heappop(heap)[1] for i in range(k)]




