def hesap_bakiyesi(bakiye, cekilen):
    if cekilen > bakiye:
        print("Bakiyeniz yetersiz.")
    else:
        kalan_bakiye = bakiye - cekilen
        print(f"Kalan bakiye: {kalan_bakiye} TL")

try:
    bakiye = float(input("Hesap bakiyesini girin: "))
    cekilen_miktar = float(input("Çekmek istediğiniz tutarı girin: "))

    hesap_bakiyesi(bakiye, cekilen_miktar)

except ValueError:
    print("Lütfen geçerli bir sayı girin.")
