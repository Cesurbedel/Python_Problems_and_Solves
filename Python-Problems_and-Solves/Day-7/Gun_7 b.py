def kazanan_teklif(teklifler):
    maksimum_teklif = max(teklifler)
    return maksimum_teklif

try:
    teklifler = []
    
    while True:
        teklif = input("Teklifi girin (Bitirmek için 'q' ya da 'Q' tuşlayin): ")
        
        if teklif.lower() == 'q':
            break
        
        teklifler.append(int(teklif))
    
    if len(teklifler) > 0:
        maksimum = kazanan_teklif(teklifler)
        print(f"Satıldı: {maksimum}")
    else:
        print("Herhangi bir teklif girilmedi.")
        
except ValueError:
    print( "Geçersiz bir değer girdiniz. Lütfen sayisal bir teklif girin veya 'q' tuşlayarak çikiş yapin." )
