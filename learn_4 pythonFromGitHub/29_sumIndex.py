import itertools


def getSumIndex(arr, target):
	'''
	传入list arr，返回和为target的索引
	'''
	arrDouble = list(itertools.combinations(arr, 2))

	sumDict = {}
	for a in arrDouble:
		indexArr = [arr.index(a[0]), arr.index(a[1])]
		sumArr = sum(a)
		if sumArr not in sumDict:
			sumDict[sumArr] = []
		sumDict[sumArr].append(indexArr) 

	return sumDict[target]


arr = [2,7,5,2,11,15]
target = 9
print(getSumIndex(arr,target))
