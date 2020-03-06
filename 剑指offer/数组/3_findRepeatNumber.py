class Solution:
	'''
	找出数组中重复的数字。


	在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

	示例 1：

	输入：
	[2, 3, 1, 0, 2, 5, 3]
	输出：2 或 3 

	'''
    def findRepeatNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        return [i[0] for i in filter(lambda x:x[1]>1, counter.items())][0]

    '''
    1. Counter(): 计算每个数字的次数
    2. 用filter筛选，filter(lambda x:x[1]>1, counter.items())，筛选items()[1]>1 的元祖
    3. 由于filter返回的是迭代器，所以要 [] 处理一下，正好将key给提出来 [i[0] for i in filter()]
    '''