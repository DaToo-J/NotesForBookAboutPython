'''
	要求：判断n是否为2的m次方
'''
def isPower1(n):
	'''
	利用移位操作
	'''
	if n < 1:
		return False
	i = 1
	while i <= n:
		if i == n:
			return True
		i <<= 1
	return False

def isPower2(n):
	'''
	如果n为2的m次方，那么n的最高位为1，n-1除了最高位都为1，将两者求 ‘&’，如果结果为0则bingo
	'''
	if n < 1:
		return False

	m = n & (n-1)

	return True if m == 0 else False


if __name__ == "__main__":
	num1 = 34
	num2 = 36
	num3 = 64
	print(isPower2(num1))
	print(isPower2(num2))
	print(isPower2(num3))