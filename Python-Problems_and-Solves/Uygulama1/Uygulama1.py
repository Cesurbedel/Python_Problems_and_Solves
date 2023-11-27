class NotDefteri:
    def __init__(self):
        self.notlar = {}

    def not_ekle(self):
        baslik = input("Not başlığını girin: ")
        icerik = input("Not içeriğini girin: ")
        self.notlar[baslik] = icerik
        print(f"Not eklendi: {baslik}")

    def not_guncelle(self):
        baslik = input("Güncellenecek notun başlığını girin: ")
        yeni_icerik = input("Yeni içeriği girin: ")
        if baslik in self.notlar:
            self.notlar[baslik] = yeni_icerik
            print(f"Not güncellendi: {baslik}")
        else:
            print("Böyle bir not bulunamadı.")

    def not_sil(self):
        baslik = input("Silinecek notun başlığını girin: ")
        if baslik in self.notlar:
            del self.notlar[baslik]
            print(f"Not silindi: {baslik}")
        else:
            print("Böyle bir not bulunamadı.")

    def notlari_listele(self):
        print("Notlarınız:")
        for baslik, icerik in self.notlar.items():
            print(f"{baslik}: {icerik}")

if __name__ == "__main__":
    not_defteri = NotDefteri()

    while True:
        print("\nYapabileceğiniz işlemler:")
        print("1. Not Ekle")
        print("2. Not Güncelle")
        print("3. Not Sil")
        print("4. Notları Listele")
        print("5. Çıkış")

        secim = input("Lütfen bir işlem seçin (1/2/3/4/5): ")

        if secim == "1":
            not_defteri.not_ekle()
        elif secim == "2":
            not_defteri.not_guncelle()
        elif secim == "3":
            not_defteri.not_sil()
        elif secim == "4":
            not_defteri.notlari_listele()
        elif secim == "5":
            print("Not Defteri uygulaması kapatılıyor.")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
