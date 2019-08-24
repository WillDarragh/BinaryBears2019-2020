

n = int(input())
for i in range(n):
	c,t = input().split('=')

	h,m = map(int,t.split(':'))

	if c[0] == 'P':
		c='Macon'
	else:
		c='Paris'

	

	if c[0] == 'M':
		h+=6
		h=h%24
	else:
		h-=6
		h+=24
		h=h%24

	x = 'AM'

	if h > 12:
		x = 'PM'
		h%=12

	print('The time in '+c+' is now '+str(h)+':'+('' if m>9 else '0')+str(m)+' '+x)

