def xodim_info(**malumotlar):
    if not malumotlar:
        return 0
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit.capitalize()} : {qiymat}")
    
malumotlari={
    "ism":input(),
    "lavozim":input(),
    "yosh":input()
}
xodim_info(**malumotlari)