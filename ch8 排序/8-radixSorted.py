import math

def radixSort(lists, radix=1000):
	'''
	基数排序
	'''
	k = int(math.ceil(math.log(max(lists), radix)))

	# radix有多大，bucket就有多少个
	# radix为10的整数倍幂，radix的位数只能大于等于lists中max的位数(不然，存不下)
	bucket = [[] for i in range(radix)]

	for i in range(1,k+1):
		for j in lists:
			# 第一次 i=0时，将各个元素按照(去掉最高位的数)的大小分别放入bucket里
			# 最高位：以radix的位数为标准。如：radix=1000， j=4321， 那么就将j放入到bucket[321]里

			# 第二次 i=1时，将各个元素按照最高位的数的大小分别放入bucket里
			# 此时，lists的元素已经是以 (去掉最高位的数)的大小 排列
			# 这时，就剩最高位的排序来完成所有排序。
			bucket[int(j/(radix**(i-1)) % (radix**i))].append(j)
		del lists[:]

		for z in bucket:
			lists += z
			del z[:]

	return lists



if __name__ == "__main__":
	lists = [323,636,32,335,141,446,38,321]
	print("Before sorting: ", lists)
	lists = radixSort(lists)
	print("After sorting : ", lists)

	print("Finished ...")


