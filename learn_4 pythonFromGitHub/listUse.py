def setCompute():
	'''
	一些关于set的计算

	Cookies：
		可用于查找出两个list中不同与相同的元素
	'''
	list1 = [1,2,3]
	list2 = [3,4,5]
	set1 = set(list1)
	set2 = set(list2)

	# print(set1 ^ set2 - set1 & set2)
	# 交集	{3}
	print('交集 ： ',set1 & set2)
	print('交集 ： ',set1.intersection(set2))

	# 并集	{1,2,3,4,5}
	print('并集 ： ',set1 | set2)
	print('并集 ： ',set1.union(set2))

	# 差集	分两种情况
	# set1 - set2	{1,2}
	s12 = set1 - set2
	print('差集 set1 - set2 ： ',s12)
	s12 = set1.difference(set2)
	print('差集 set1 - set2 ： ',s12)
	# set2 - set1	{4,5}
	s21 = set2 - set1
	print('差集 set2 - set1 ： ',s21)
	s21 = set2.difference(set1)
	print('差集 set2 - set1 ： ',s21)

	# 对称差集	{1,2,4,5} = 并集 - 交集
	print('对称差集 ： ',set1 ^ set2 )
	print('对称差集 ： ', set1.symmetric_difference(set2))


def listCut():
	'''
	给一个list去重，并保留原来的元素顺序
	'''

	l1 = ['b','a','c','d','c','a','a']
	l2 = list(set(l1))
	l2.sort(key=l1.index)	#l2 = sorted(set(l1),key=l1.index)
	print(l2)


def listToSet(arr):
	'''
	传入 arr 序列，利用字典的方法去重
	'''
	b = {}
	b = b.fromkeys(arr)
	return b
	
arr = [2,7,5,2,11,15]
# print(listToSet(arr))

def listParse(num):
	'''
	练习 ‘列表解析’
	返回：是偶数，且在num的index是偶数
	'''
	return [i for i in num if i % 2 == 0 and num.index(i) % 2 == 0]

	# for i in num:
	# 	if i % 2 == 0 and num.index(i) % 2 == 0:
	# 		return i

num = [0,1,2,3,4,5,6,7,8,9]
# print(listParse(num))

def fun1(str1):
	'''
	给定一个任意长度数组，实现一个函数
	让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序.
	如字符串'1982376455',变成'1355798642'
	'''
	odd = [i for i in str1 if int(i) % 2 == 1]
	odd.sort()

	even = [i for i in str1 if int(i) % 2 == 0]
	even.sort(reverse = True)

	return ''.join(odd)+''.join(even)

str1 = '1982376455'
# print(fun1(str1))

def genIntList():
	'''
	列表解析
	请用一行代码 实现将1-N 的整数列表以3为单位分组
	'''
	N =100
	print ([[x for x in range(1,100)] [i:i+3] for i in range(0,100,3)])
	# 先range出1-99，再通过下标切片来进行分组
	

genIntList()