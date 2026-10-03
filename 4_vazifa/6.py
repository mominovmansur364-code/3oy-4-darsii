n = int(input())
sonlar = list(map(int, input().split()))


def ijobiy_yigindi(*lst):
    return sum(filter(lambda x: x > 0, lst[:n]))

print(ijobiy_yigindi(*sonlar))