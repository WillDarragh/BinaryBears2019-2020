
suf = {	'ing':'to actively ',
	'ize':'change into ',
	's':'multiple instances of ',
	'er':'one who ',
	'tion':'the process of '}

pre = { 'anti':'against ',
	'post':'after ',
	'pre':'before ',
	'un':'not ',
	're':' again'	}

# Special : re, er, tion

for n in range(int(input())):
	
	word = input()

	P = ''
	S = ''

	for p in pre.keys():
		if word.startswith(p):
			P = p
			word = word[len(p):]
			break
	
	for s in suf.keys():
		if word.endswith(s):
			S = s
			word = word[:(-1*len(s))]
	
	result = word

	if S:
		result = suf[S]+result

	if S == 'tion':
		result += 'ing'
	elif S == 'er':
		result += 's'

	if P == 're':
		print(result+pre[P])
	elif P:
		print(pre[P]+result)
	else:
		print(result)
