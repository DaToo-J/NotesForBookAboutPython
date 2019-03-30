'''
	要求：将字符串‘1234’，转换成int类型的 1234
'''

def strToInt1(str1):
	'''
	对字符串进行拆分，并计算出真实值
	'''
	num = 0
	for s in str1:
		for j in range(10):
			if s == str(j):
				num = num * 10 + j
	print(num)
	print(type(num))


def strToInt2(str1):
	'''
	使用eval函数，将字符串当作表达式求得结果
	'''
	str2 = str1 + ' * 1'
	num  = eval(str2)
	print(num)
	print(type(num))

str1 = '1234'
strToInt1(str1)
strToInt2(str1)
