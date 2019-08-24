


n = int(input())

pre = {	'anti':'against ',
	'post':'after ',
	'pre':'before ',
	're':' again',
	'un':'not '	}

suf = {	'er':'one who ',
	'ing':'to actively ',
	'ize':'change into ',
	's':'multiple instances of ',
	'tion':'the process of '	}

things = list(pre.keys())+list(suf.keys())

for i in range(n):
	line = input()
	new = line
	for p in pre.keys():
		if p == line[:(len(p))]:
			if p == 're':
				new = line[2:]+pre[p]
			else:
				new = new.replace(p,pre[p])

	for s in suf.keys():
		if s in line:
			if s == 'er':
				new = 'one who '+new.replace(s,'')+'s'
			if s == 'tion':
				new = suf[s] + new.replace(s,'')+'ing'
			else:
				new = suf[s] + new.replace(s,'')
	print(new)

