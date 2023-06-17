from math import *
for u in range(int(input())):
   n=int(input())
   l=list(map(int,input().split()))
   x,y=0,0
   s=0
   while(y<n):
     if(l[y]>=l[x]):
       y=y+1
     else:
       s+=(y-x+1)*l[x]-l[y]
       x=y
       s+=(n-x)*l[x]-l[n-1]
       if(s<=0):
         print(0)
       else:
         print(s)