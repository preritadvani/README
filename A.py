t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(set(a))
    l=len(b)
    c=[]
    for k in range(l):
        c.append(1)
    d=0
    for j in range(n-1):
        if a[j+1]==a[j]:
            c[d]+=1
        else: d+=1
    c.sort(reverse=True)
    d=[]
    for m in range(l):
        d.append(c[m]*(m+1))
    ans.append(max(d))
for i in range(t):
    print(ans[i])