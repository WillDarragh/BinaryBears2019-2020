import re, sys

V = {}
for n in range(int(input())):
	v = input()
	V[v] = 'cody'+str(n)

for line in sys.stdin:
	line = line.rstrip()
	if line[:2] == '//':
		print()
		continue
	qs = [m.start() for m in re.finditer('"', line)]
	pos = [[qs[i],qs[i+1]] for i in range(0,len(qs),2)]

	strings = []
	escapes = []	
	for p in pos:
		s,f = p
		string = line[s+1:f]
		strings.append('"'+string+'"')
		escapes.append('"'+''.join([r'\x'+(hex(ord(c))[2:]).upper() for c in string])+'"')

	for s,e in zip(strings,escapes):
		line = line.replace(s,e)
	
	line = re.sub(r'[ \t]+',' ',line)

	for v in V.keys():
		p = re.compile(r'\W'+v+r'\W')
		for i in re.findall(p, line):
			line = line.replace(i, i[0]+V[v]+i[-1])
		p = re.compile(r'^'+v+r'\W')
		for i in re.findall(p, line):
			line = line.replace(i, V[v]+i[-1])
		p = re.compile(r'\W'+v+r'$')
		for i in re.findall(p, line):
			line = line.replace(i, i[0]+V[v])

	print(line)
