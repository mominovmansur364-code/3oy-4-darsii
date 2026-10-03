def daraja(son,n=2):
    return son**n

qiymat=list(map(int,input().split()))

if len(qiymat)==2:
    print(daraja(qiymat[0],qiymat[1]))
else:
    print(daraja(qiymat[0]))