#!/usr/bin/python
# -*- coding: utf-8 -*-

def isValid( s):
	# print(s)
	stack = []
	for i in s:
		if len(stack) == 0:
			stack.append(i)
		elif isPair(stack[-1], i):
			stack.pop()
		else:
			stack.append(i)

	print('stack: ',stack)

	if len(stack) == 0:
		return True
	else: 
		return False

def isPair(a,b):
	if a == '(' and b == ')':
		return True
	elif a == '{' and b == '}':
		return True
	elif a == '[' and b == ']':
		return True
	else:
		return False

# stack = []
# print(stack[-1])
s = "["
# print(s[-1])
isValid(s)