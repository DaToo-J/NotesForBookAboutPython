'''
要求：求d的n次方
思路：
	1. n = 0, 为1
	2. n = 1, 为d
	3. n > 0, 
			先求tmp = d的 n/2 次方
			n为奇数：tmp * tmp * d
			n为偶数：tmp * tmp
	4. n < 0,
			同理，只不过是1/tmp
'''
def power(d,n):
	if n == 0:
		return 1
	if n == 1:
		return d

	tmp = power(d, int(abs(n)/2))
	if n > 0: 
		if n % 2 == 1:
			return tmp*tmp*d
		else:
			return tmp*tmp
	else:
		if n % 2 == 1:
			return 1/(tmp*tmp*d)
		else:
			return 1/(tmp*tmp)
if __name__ == "__main__":
	print(power(3,5))
	# print(abs(5)/2)