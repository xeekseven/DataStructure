def  insertsort(A):#数组的下标从1开始
	nowp=1;
	lenth=len(A)-1
	while(lenth-nowp>=0):
		key=A[nowp]
		opp=nowp-1
		nowp=nowp+1
		while opp>0 and key<A[opp]:#大于就停止后移
			A[opp+1]=A[opp]
			opp=opp-1
		A[opp+1]=key
		
	return A
