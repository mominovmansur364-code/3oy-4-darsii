def orta_arifmetik(*sonlar):
    if not sonlar:
        return 0
    return sum(sonlar)/len(sonlar)

sonlar=list(map(int,input().split()))
print(orta_arifmetik(*sonlar))