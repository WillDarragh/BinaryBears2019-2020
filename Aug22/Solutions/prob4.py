
pre = {
	"anti": "against ",
	"post": "after ",
	"pre": "before ",
	"re": " again",
	"un": "not "
}
suf = {
	"er": "one who ",
	"ing": "to actively ",
	"ize": "change into ",
	"s": "multiple instances of ",
	"tion": "the process of "
}

cases = int(input())
for c in range(cases):
	line = input()
	result = "%s"
	
	for key, val in suf.items():
		if line.endswith(key):
			result = val + result
			if key == "er":
				result = result.replace("%s", "%ss")
			elif key == "tion":
				result = result.replace("%s", "%sing")
			line = line.replace(key, "", 1)

	for key, val in pre.items():
		if line.startswith(key):
			if key == "re":
				result = result + val
			else:
				result = val+result
			line = line.replace(key, "", 1)
			
	print(result % (line))
