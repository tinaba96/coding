N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort()

ans = 1001001001
i=0
j=0

while i!=N and j!=M:
    ans=min([ans,abs(A[i]-B[j])])
    if A[i]<B[j]:
        i+=1
    else:
        j+=1
    
print(ans)
