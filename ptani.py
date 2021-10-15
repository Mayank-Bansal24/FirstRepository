k=int(input())
for i in range(0,k):
    n=int(input())
    li= list(map(int,input().strip().split()))[:n]
    sli=sorted(li)
    X=[]
    M=[]
    for x in range(n-1):
        for m in range(n):
            if sli[x]==li[m]:
                if m-x>0:
                    X.append(x+1)
                    M.append(m+1)
    print(len(X))
    for x in range(0,len(M)):
        print(X[x],M[x],M[x]-X[x])
