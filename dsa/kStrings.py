a = [0,0]

def K_strings(n,k):
	if n<1:
		print(a)
	else:
		for j in range(0,k):
			a[n-1]=j
			K_strings(n-1,k)

K_strings(2,2)
