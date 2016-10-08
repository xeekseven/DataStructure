
def	mergesort(A,l,r):
	
	#l-左 ，m-中间，r-右
	if l<r:
		m=(l+r)//2
		mergesort(A,l,m)
		mergesort(A,m+1,r)
		A=mergeop(A,l,m,r)
		#print(A)
	return A

def mergeop(A,l,m,r):
	ll=m-l+1
	lr=r-m
	L=[0]
	lstart=1
	rstart=1

	R=[0]
	while(ll-lstart>=0):
		L.append(A[l+lstart-1])
		lstart+=1
	L.append(10000)
	#print(L)
	while(lr-rstart>=0):
		R.append(A[m+rstart])
		rstart+=1
	R.append(10000)
	#print(R)

	#两个数组合二为一
	i=1
	j=1
	k=l
	while r-k>=0:
		
		if L[i]==10000 and R[j]==10000:
			break
		'''
		if i==ll+1 or r==lr+1:
			break
		'''
		if(L[i]<=R[j]):
			A[k]=L[i]
			i+=1
		else:
			A[k]=R[j]
			j+=1
		k+=1
		#print('A[K-1]:',A[k-1])
	'''
	if i != ll+1:
		while(ll-i>=0):
			A[k]=L[i]
			print(A[k])
			i+=1
			k+=1
	if j != lr+1:
		while(lr-j>=0):
			A[k]=R[j]
			print(A[k])
			j+=1
			k+=1
	'''
	return A





		
