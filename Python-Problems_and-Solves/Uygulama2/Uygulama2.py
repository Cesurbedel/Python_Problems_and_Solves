import random

# Kelime listesi
kelimeler = ["python", "programlama", "oyun", "eğlence", "öğrenme"]

# Kelime listesinden rastgele bir kelime seçme işlevi
def kelime_sec(kelimeler):
    return random.choice(kelimeler)

# Oyun değişkenlerini tanımlama
secilen_kelime = kelime_sec(kelimeler)
tahmin_edilen_harfler = []
tahmin_hakki = 6
kazanma_durumu = False

# Oyun döngüsü
def oyunu_baslat():
    global secilen_kelime, tahmin_edilen_harfler, tahmin_hakki, kazanma_durumu
    print("Adam Asmaca Oyununa Hoş Geldiniz!")

    while tahmin_hakki > 0 and not kazanma_durumu:
        # Kalan tahmin hakkını ve tahmin edilen harfleri göster
        print(f"Kalan tahmin hakkınız: {tahmin_hakki}")
        print(f"Tahmin edilen harfler: {' '.join(tahmin_edilen_harfler)}")

        # Kullanıcıdan tahmin al
        tahmin = input("Bir harf tahmini yapın: ").lower()

        # Geçerli bir tahmin mi kontrol et
        if len(tahmin) == 1 and tahmin.isalpha():
            # Daha önce tahmin edilen bir harf mi kontrol et
            if tahmin in tahmin_edilen_harfler:
                print("Bu harfi zaten tahmin ettiniz. Lütfen farklı bir harf deneyin.")
            elif tahmin in secilen_kelime:
                # Tahmin edilen harfi ekle
                tahmin_edilen_harfler.append(tahmin)
                print("Harika! Doğru tahmin!")
            else:
                # Tahmin edilen harf yanlış ise tahmin hakkını azalt
                tahmin_hakki -= 1
                print("Üzgünüm, yanlış tahmin.")
        else:
            print("Geçersiz giriş. Lütfen tek bir harf girin.")

        # Kazanma durumunu kontrol et
        if set(secilen_kelime).issubset(set(tahmin_edilen_harfler)):
            kazanma_durumu = True

    # Kazanma veya kaybetme durumuna bağlı olarak sonucu göster
    if kazanma_durumu:
        print(f"Tebrikler! Kelimeyi buldunuz. Kelime: {secilen_kelime}")
    else:
        print(f"Oyun bitti. Doğru kelime: {secilen_kelime}")

# Main
if __name__ == "__main__":
    oyunu_baslat()