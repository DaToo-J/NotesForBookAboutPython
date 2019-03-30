from collections import Counter
def sortDict(d):
	'''
	输入一个字典d
	返回排序后的d
	'''
	return sorted(d.items(), key=lambda x:x[1])

	# Cookies：lambda的使用
	# lambda express1 : express2
	# express1 : 输入，参数列表
	# express2 : 输出，表达式的值

	# 拓展：
	# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
	# 按 ‘age’ 大小排序
	# key = lambda x:x['age']
d= {'a':24,'g':52,'i':12,'k':33}
# print(sortDict(d))




def strToDict(str1):
	'''
	输入一个字符串
	返回该字符串相对应的字典
	'''
	return  {k:int(v) for t in str1.split("|") for k,v in (t.split(":"),)}

	# Cookies：字典推导式的使用
	# d = {key,value for (key,value) in iterable}

	# 思路：
	# for t in str1.split("|"):
	# 	for k,v in (t.split(":"),):
	# 		print(k,v)

str1 = "k:1|k1:2|k2:3|k3:4"
# print(strToDict(str1))


def listToSet(arr):
	'''
	传入 arr 序列，利用字典的方法去重
	'''
	b = {}
	b = b.fromkeys(arr)
	return b

arr = [2,7,5,2,11,15]
# print(listToSet(arr))


def countStr(str1):
	'''
	统计字符串str1中的字符次数

	map(function, iterable, ...)
	map用法：function接收iterable序列作为参数
	
	most_common(n)
	用法：统计dict中n个频率最高的元素, 

	print(Counter(str1))					# Counter({'A': 4, 'C': 3, 'B': 2})
	print(Counter(str1).most_common())		# [('A', 4), ('C', 3), ('B', 2)]， 元素为tuple
	'''

	return " ".join(map(lambda x: x[0] + str(x[1]), Counter(str1).most_common()))
str1 = "AAABBCCAC"
print(countStr(str1))