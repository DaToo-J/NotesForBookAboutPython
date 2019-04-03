'''
	要求：判断n是否为某个自然数的平方
'''
def isPower1(n):
	'''
	思路：对小于n的非零自然数求平方，看是否等于或大于n
	'''
	if n <= 0:
		return False

	for i in range(1,n):
		tmp = i * i 
		if tmp == n:
			return True
		elif tmp > n:
			return False

def isPower2(n):
	'''
	二分查找法
	mid = 1和n的中位数，将1和n平分
	如果mid的平方大于n，则在前半段继续查找；
	如果mid的平方小于n，则在后半段继续查找。
	'''
	low = 1
	high = n
	while low < high:
		mid = int((low + high) / 2)
		print(mid)
		power = mid * mid 
		if power > n:
			high = mid - 1
		elif power < n:
			low = mid + 1
		else:
			return True
	return False

def isPower3(n):
	'''
	利用平方数规律:
		(n+1)^2 = 1 + 3 + 5 + 7 + ... + (2*n+1)
		Sn = (1 + (2*n+1)) / 2 = (n+1)^2
	思路：
		一次减1,3,5...,直到n为 0 或 负
	'''
	minus = 1
	while n > 0:
		n = n - minus
		if n == 0:
			return True
		elif n < 0:
			return False
		else:
			minus += 2

if __name__ == "__main__":
	num1 = 34
	num2 = 36
	print(isPower3(num1))
	print(isPower3(num2))