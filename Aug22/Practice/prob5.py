
import string

LETS = string.ascii_uppercase

r,c = map(int,input()[1:].split('C'))


while(r!=0 and c!=0):


	C = ''
	rem = c-1
	while(rem>=0):
		#print(rem)
		C = LETS[(rem%26)]+C
		rem = (rem//26)-1	

	
	print(C+str(r))

	r,c = map(int,input()[1:].split('C'))
