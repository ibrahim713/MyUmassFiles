a = [1,2,3,4,5]
print a
n = len(a)
for i in range(n // 2):
    a[i], a[n-1-i]=a[n-1-i],a[i]
print a
