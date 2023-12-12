	#lösung 1:
def a(nums):
	return sum(range(0,len(nums)+1)) - sum(nums)
	#lösung 2:
def b(nums):
	return list(set(range(0,len(nums)+1)) - set(nums))[0]
	#lösung 3: nutzt bitwise function XOR  ^=
def c(nums):
    nums = nums + list(range(0,len(nums)+1))
    ans = 0
    for i in nums:
        ans ^= i
    return ans