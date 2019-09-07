# Prob3 Cipher

from sys import stdin
import string as s

ups = s.ascii_uppercase
lows = s.ascii_lowercase


for line in stdin.readlines():
	if line[0] == '#':
		break
	keys = list(map(int, line.split()[:-2]))
	mode, message = line.split()[-2:]
	
	if mode == 'D':
		keys = list(map(lambda x: -1*x,keys))

	for i in range(len(keys)):
		let = message[i]
		if let.isupper():
			alp = ups
		else:
			alp = lows
		new_let = alp[(alp.index(let)+keys[i])%26]
		print(new_let,end='')
	print()
