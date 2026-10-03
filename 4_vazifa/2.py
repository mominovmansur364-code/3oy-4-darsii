
def katta_son(a,b):
    return a if a>b else b

a, b = map(int, input().split())
print(katta_son(a,b))