ones = ['one','two','three','four','five','six','seven','eight','nine']

teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen']+[o+'teen' for o in ones[5:]]

tens = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

hundred = ones+teens

for t in tens:
	hundred.append(t)
	for o in ones:
		hundred.append(t+'-'+o)

hunds = [o+' hundred' for o in ones]

thousand = []+hundred

for h in hunds:
	thousand.append(h)
	for n in hundred:
		thousand.append(h+' '+n)

thousand = ['zero']+thousand

N = int(input())
for n in range(N):

	d,f = input().split('.')

	dollars = ''

	mil = d[-9:-6]
	if mil and int(mil):
		dollars += thousand[int(mil)] + ' million '

	tho = d[-6:-3]
	if tho and int(tho):
		dollars += thousand[int(tho)] + ' thousand '

	hun = d[-3:]
	if not (dollars and int(hun)==0):
		dollars += thousand[int(hun)]+' '

	print('{}and {}/100 dollars'.format(dollars,f))
