def yetkazish_haqi(narx, haq=5000):
  return narx + haq


malumotlar = list(map(int, input().split()))

if len(malumotlar) == 1:
  print(yetkazish_haqi(malumotlar[0]))
elif len(malumotlar) == 2:
  print(yetkazish_haqi(malumotlar[0], malumotlar[1]))