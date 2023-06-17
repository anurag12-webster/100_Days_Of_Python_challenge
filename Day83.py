z=0
while z==0:
    h=int(input())
    if h==0:
        break
    n=(1<<h)-1
    p=[0]*(n+10)
    v=[ int(x) for x in input().split() ]
    for i in range(n-1,-1,-1):
        if 2*i+1 >=n:
            p[i]=v[i]
        else:
            p[i]=v[i]*max(p[2*i+1],p[2*i+2])
            ans=p[0]%1000000007
            print(ans)