import datetime

def dayOfYear(y,m,d):
	'''
	输入年月日，
	打印这一天是这一年的第几天
	'''
	date1 = datetime.date(year=int(y), month=int(m), day=int(d))
	date2 = datetime.date(year=int(y), month=1, day=1)

	print((date1-date2).days+1)

y = 2018
m = 3
d = 23

dayOfYear(y,m,d)
