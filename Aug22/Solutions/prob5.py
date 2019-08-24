import string

LETS = string.ascii_uppercase

r,c = map(int,input()[1:].split('C'))

while(r and c):
	
	C = ''
	rem = c-1
	while(rem>=0):
		C = LETS[(rem%26)]+C
		rem = (rem//26)-1	

	print(C+str(r))
	r,c = map(int,input()[1:].split('C'))
