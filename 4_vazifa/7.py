def talaba_info(**malumotlar):
  for kalit, qiymat in malumotlar.items():
    print(f"{kalit.capitalize()} : {qiymat}")

ism_kirit = input()
kurs_kirit = input()
shahar_kirit = input()

talaba_info(ism=ism_kirit, kurs=kurs_kirit, shahar=shahar_kirit)