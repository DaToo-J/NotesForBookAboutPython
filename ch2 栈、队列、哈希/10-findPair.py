'''
要求： 给定一个数组，找出是否有两个数对(a,b) 和 (c,d)，使得 a+b=c+d，并且a、b、c、d都不同。
思路：
		1. 利用字典来保存 数对和数对的和。 {'数对的和': 数对}
		2. 当有一个数对的和已经在字典中出现，那么，不就巧了吗
'''

import itertools

def findPair(arr):
	pairsList = list(itertools.combinations(arr, 2))
	sumPairs = dict()
	for p in pairsList:
		sumP = p[0] + p[1]
		if sumP not in sumPairs:
			sumPairs[sumP] = [p[0], p[1]]
		else:
			pp = sumPairs[sumP]
			print(pp[0],'+',pp[1] ,' = ',p[0], '+', p[1])
			return True
	return False

if __name__ == "__main__":
	arr = [3,5,6,23,76,31,32]
	findPair(arr)