#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2

'''

def calculate(s):
	stack, tmp = [], []
	for c in s:
		if c == "(" :
			if tmp:
				stack.append(tmp)
				tmp = []
			tmp.append(c)
		elif c == ")":
			tmpRes = cal_tmp(tmp)
			if stack:
				stack[-1].append(tmpRes)
				tmp = stack.pop()
			else:
				tmp = [tmpRes]
		else:
			tmp.append(c)

	return  cal_tmp(tmp)

def cal_tmp(tmp):
	res = 0
	n = 0
	op = 1
	for t in range(len(tmp)):
		if tmp[t] == "+":
			res += n * op
			op = 1
			n = 0 
		elif tmp[t] == "-":
			res += n * op
			op = -1
			n = 0
		elif tmp[t] != "(":
			n = n * 10 + int(tmp[t])
	res += n * op
	return str(res)


# s = "(1+(4+5+2)-3)+(6+8)"
s = "2-(5-6)"
res = calculate(s)
print(res)
