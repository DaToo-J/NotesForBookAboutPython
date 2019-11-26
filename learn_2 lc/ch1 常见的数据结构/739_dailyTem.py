#!/usr/bin/python
# -*- coding: utf-8 -*-
def dailyTemperatures(T):
	stack = []
	r = [0] * len(T)
	output = []
	for i, t in enumerate(T):
		while stack and T[stack[-1]] < t: 	# 只要栈顶元素 < 即将入栈元素，就一直弹出、继续判断
											#  T[stack[-1]] ：栈顶元素，stack记录的已入栈元素的下标
											# t：即将入栈元素
			r[stack.pop()] = i - stack[-1]

		stack.append(i) 	# 用stack同步记录元素的下标，stack = [0,1,2,3,4,...], 
	return r


T = [73,74,75,71,69,72,76,73]       
t = dailyTemperatures(T)
print(t)