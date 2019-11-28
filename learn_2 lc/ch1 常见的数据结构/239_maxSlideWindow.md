## 0. [LeetCode 239 题解链接](https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-shuang-duan-dui-lie-de-pythons/)

# 1. 题目描述

- 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
  你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

- 返回滑动窗口中的最大值。

- 示例:

> 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
> 输出: [3,3,5,5,6,7] 



# 2. 思路

- 利用双端队列
- 要点：
  - 确保队列的队首为当前窗口的max；
  - 如果队首在窗口之外，则弹出窗口；
  - 每遍历到新元素时，都需要和队尾元素比较；
    - 队尾 < 新元素：去队尾，直到队尾不小于新元素
    - 否则，直接将新元素添加到队尾



| nums  | 1    | 3    | -1   | -3      | 5    | 3    | 6    | 7    |
| ----- | ---- | ---- | ---- | ------- | ---- | ---- | ---- | ---- |
| index | 0    | 1    | 2    | 3       | 4    | 5    | 6    | 7    |
| res   |      |      | 3    | 3       | 5    | 5    | 6    | 7    |
| tmp   | 1    | 3    | 3,-1 | 3,-1,-3 | 5    | 5,3  | 6    | 7    |

- index = 1时：新元素3 > 队尾1，则去队尾，加入新元素
- index = 4时：队首在窗口之外，先弹出队首。新元素5再和[-1,-3]的队尾比较...



```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

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
```



