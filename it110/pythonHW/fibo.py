
def fibo(n):
	#stop cases below
	if n == 0:
	 	return 0
	if n == 1:
		return 1
	#recursive case
	return fibo(n-1) + fibo(n-2)
#test case, print all fibo numbers from 0- n
n=40
for i in range(n+1):
	print fibo(i)
