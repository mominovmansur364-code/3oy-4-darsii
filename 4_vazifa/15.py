
    
Sonlar=list(map(int,input().split()))

natija=list(map(lambda x:x**2 if x>=0 else x,Sonlar))

print(natija)
