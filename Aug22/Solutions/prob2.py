for n in range(int(input())):
	
	c,t = input().split('=')
	h,m = map(int,t.split(':'))
	
	if c[0]=='P':
		c='Macon'
	else:
		c='Paris'

	if c[0]=='M':
		h += 24
		h -= 6
	else:
		h += 6
	h %= 24
	
	e = 'AM'
	if h > 12:
		h -= 12
		e = 'PM'
	if not h:
		h = 12	

	print('The time in {} is now {}:{:0>2} {}'.format(c,h,m,e))
