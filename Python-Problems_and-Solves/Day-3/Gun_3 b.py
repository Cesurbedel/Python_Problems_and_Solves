def acik_mi(gun, saat):
    if gun >= 1 and gun <= 5:  # Pazartesi'den Cuma'ya kadar olan günler
        if saat >= 10 and saat < 21:
            return "Açık"
        else:
            return "Kapalı"
    else:
        return "Kapalı"  # Cumartesi ve Pazar

try:
    gun = int(input("Haftanın gününü girin (Pazartesi için 1, Salı için 2, ... Pazar için 7): "))
    saat = int(input("Saat bilgisini girin (0-23 arası): "))

    durum = acik_mi(gun, saat)
    print("Mağaza", durum)

except ValueError:
    print("Lütfen geçerli bir sayı girin.")
