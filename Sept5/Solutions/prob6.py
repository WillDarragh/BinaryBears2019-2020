# Prob6 Chinese

Z = ['snake','horse','sheep','monkey','rooster','dog','pig','rat','ox','tiger','rabbit','dragon']

for r in range(int(input())):
	y = int(input())
	print(f'{y} is the year of the {Z[(y-1965)%12]}')
