#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 

'''
import collections

def maxSlidingWindow(nums, k):
	tmp = collections.deque()
	res = []
	for i, t in enumerate(nums):
		if tmp and (i - tmp[0]) >= k:
			tmp.popleft()
		while tmp and nums[tmp[-1]] < t: 	
			tmp.pop()

		tmp.append(i) 
		if i >= (k-1):
			res.append(nums[tmp[0]])
		print(i, tmp, res)
	return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3

nums = [1,-1]
k = 1

res = maxSlidingWindow(nums, k)
print(res)

