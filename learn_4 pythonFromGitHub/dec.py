
def abc1():
	def abc():
		print('abc in abc')
	print('abc1')
	return abc

# abc1()()


def add(m):
	def temp(n):
		return m+n
	return temp

# print(add(1)(5))



'''
闭包closure：
	1.必须有内嵌函数
	2.内嵌函数必须引用外部函数中的变量
	3.外部函数返回值必须是内嵌函数

装饰器dec：
	带有函数作为参数并返回一个新函数的闭包
'''

def outer():
	'''
	closure:
		1. 内嵌函数 inner
		2. 引用外部函数变量：x
		3. 外部函数返回内嵌函数：return innner
	'''
	x = 1
	def inner():
		print(x)
		# return 'this is inner func'
	return inner
print(outer()())

