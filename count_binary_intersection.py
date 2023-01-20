from sys import getsizeof

b = input('binary:')
n = input('decimal:')
b = ['1' for i in range(68*10)]
b = ''.join(b)
print('len(b)',len(b))
b = int(b,base=2)
n = int(n)
cnt = 0
print('size of b', getsizeof(b))
print(len(str(b)))
for k in range(1,n+1):
    if n&b>0:
        cnt += 1
print(cnt)




exit(0)
for k in range(len(b)):
    ch = b[-k-1]
    m = 2**k
    L = n-m+1
    if ch == '1':
        cnt += L//(2*m)*m+min(m, L % (2*m))
    print(ch,cnt)
print(cnt)


